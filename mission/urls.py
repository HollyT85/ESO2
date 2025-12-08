"""
URL configuration for mission app.
"""
from django.urls import path
from . import views

app_name = 'mission'

urlpatterns = [
    path('', views.plan, name='plan'),
    path('mission/', views.mission, name='mission'),
    path('work/', views.work, name='work'),
    path('gallery/', views.gallery, name='gallery'),
]
