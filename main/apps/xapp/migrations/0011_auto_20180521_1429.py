# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xapp', '0010_auto_20180521_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=25)),
                ('desc', models.CharField(max_length=8)),
                ('startdate', models.TextField(max_length=50)),
                ('enddate', models.TextField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_destination', to='xapp.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trips',
            name='travelers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_traveler', to='xapp.User'),
        ),
        migrations.AddField(
            model_name='destination',
            name='triptaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='xapp.User'),
        ),
    ]