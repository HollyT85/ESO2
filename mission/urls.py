"""
URL configuration for mission app.
"""
from django.urls import path
from . import views

app_name = 'mission'

urlpatterns = [
    path('', views.mission, name='mission'),
]
