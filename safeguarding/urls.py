"""
URL configuration for safeguarding app.
"""
from django.urls import path
from . import views

app_name = 'safeguarding'

urlpatterns = [
    path('', views.safeguarding, name='safeguarding'),
]
