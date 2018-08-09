from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def indexlogin(request):
    # Product.objects.all().delete()
    # Sales.objects.all().delete()
    return render(request, 'xapp/login.html')


def logout(request):
    request.session.clear()
    return redirect('/')


def loginprocess(request):
    results = User.objects.loginValidator(request.POST)
    # print(results)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='login')
        return redirect('/')


def register(request):
    return render(request, 'xapp/register.html')


def create(request):
    print(request.POST)
    results = User.objects.regValidator(request.POST)
    print(results)
    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='register')
            return redirect('/register')


def add(request, user_id=None):
    return render(request, 'xapp/addtrip.html')


def addtripprocess(request, user_id=None):
    results = Trip.objects.tripValidator(request.POST, request.session['id'])
    print(results)
    if results[0]:
        return redirect('/dashboard/{}'.format(request.session['id']))
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='triperror')
            return redirect('/add/{}'.format(request.session['id']))


def showtrip(request, x):
    return render(request, 'xapp/showtrip.html', {'info': Trip.objects.get(id=x)})


def dashboard(request, user_id=None):
    if 'id' not in request.session:
        return redirect('/')
    #original 
    #mytrips = Trip.objects.filter(planner_id=request.session['id'])
    mytrips = User.objects.get(id=request.session['id']).joins.all()
    trips = Trip.objects.exclude(bookings = request.session['id'])

    context = {
        'trips': trips,
        'mytrips': mytrips,
    }
    return render(request, 'xapp/dashboard.html', context)

def join(request, x):
    user = User.objects.get(id=request.session['id'])
    trip = Trip.objects.get(id=x)

    user.joins.add(trip)
    
    return redirect('/dashboard')

