"""
URL configuration for events app.
"""
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='events'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('previous', views.previous, name='previous'),
    path('fossilfest', views.fossilfest, name='fossilfest'),
    path('staithes', views.staithes, name='staithes'),
    path('redcar', views.redcar, name='redcar'),



]
