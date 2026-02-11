"""
URL configuration for team app.
"""
from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team, name='team'),
    path('memoriam/', views.memoriam, name='memoriam'),
    path('trustees/', views.trustees, name='trustees'),

]
