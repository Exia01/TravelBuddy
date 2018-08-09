from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt
from datetime import datetime

now = str(datetime.now())

class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []
        if len(form['name']) < 3:
            errors.append("Name must have at least 3 characters.")
        if len(form['username']) < 2:
            errors.append("Username must have at least 3 characters.")
        elif User.objects.filter(username=form['username']):
             errors.append("Account already exists.")
        if len(form['pass']) < 5:
            errors.append("Password must have at least 5 characters.")
        elif form['pass'] != form['confirmpass']:
            errors.append("Password and confirm password must match.")

        if not errors:
            hash1 = bcrypt.hashpw(form['pass'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                name=form['name'], username=form['username'], password=hash1)
            return (True, user)
        else:
            return (False, errors)

    def loginValidator(self, form):

        errors = []

        if not form['username'] or not form['pass']:
            errors.append('username  and password are required.')
        elif not User.objects.filter(username=form['username']):
            errors.append('Please register first')
        elif len(form['pass']) < 5:
            errors.append('Password must have at least 5 characters.')
        else:
            user = User.objects.filter(username=form['username']) 
            if not bcrypt.checkpw(form['pass'].encode(), user[0].password.encode()):
                errors.append('Password does not match record.')

        if not errors:
            return (True, user[0])
        else:
            return (False, errors)


class TripValidator(models.Manager):

    def tripValidator(self, form, id):

        errors = []

        if not form['destination']:
            errors.append('Destination cannot be empty.')
        if not form['desc']:
            errors.append('Description cannot be empty.')
        if len(form['desc']) < 5:
            errors.append('User must be at least 5 characters.')

        elif form['startdate'] < now:
            errors.append('Start date must be in the future')

        if not form['endate']:
            errors.append('End date is required')
        elif form['endate'] < now:
            errors.append('End date must be in the future')

        if form['endate'] < form['startdate']:
            errors.append('End date must be after start date')

        if not errors: #ask why she did it that way?
            planner = User.objects.get(id=id)
            trip = Trip.objects.create(
                destination=form['destination'], startdate=form['startdate'], enddate=form['endate'], desc=form['desc'], planner=planner)

            planner.joins.add(trip)

            return (True, trip)
        else:
            return (False, errors)
        
        

class User(models.Model):
    name = models.CharField(max_length=8)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<User {}| {} {}'.format(self.id, self.name, self.username)

    objects = UserManager()


class Trip(models.Model):
    destination = models.CharField(max_length=25)
    desc = models.CharField(max_length=8)
    startdate = models.DateField()
    enddate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    planner = models.ForeignKey(User, related_name='trips')
    bookings = models.ManyToManyField(User, related_name='joins')

    def __repr__(self):
        return '<Destination {}| {} {} | {} {}'.format(self.id, self.destination, self.desc, self.startdate, self.enddate)

    objects = TripValidator()
