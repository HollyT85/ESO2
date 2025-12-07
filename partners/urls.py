"""
URL configuration for partners app.
"""
from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners, name='partners'),
]
