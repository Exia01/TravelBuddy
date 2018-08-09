from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexlogin), #start as login
    url(r'^register$', views.register),#register page
    url(r'^create$', views.create), #registers the user
    url(r'^dashboard/$', views.dashboard),#main page
    

    url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard), #dashboard redirect with user.
    url(r'^add/(?P<user_id>\d+)$', views.add),# add a trip 
    url(r'^showtrip/(?P<x>\d+)$', views.showtrip),# show a trip 
    url(r'^jointrip/(?P<x>\d+)$', views.join),# show a trip 
    
    url(r'^loginprocess$', views.loginprocess), #logs in the user
    url(r'^addtripprocess$', views.addtripprocess),# add the trip process
    url(r'^logout$', views.logout),#log out
]
