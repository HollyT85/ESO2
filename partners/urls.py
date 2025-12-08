"""
URL configuration for partners app.
"""
from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners, name='partners'),
    path('patrons', views.patrons, name='patrons'),
    path('significantpartners', views.sig, name='significantpartners'),
    path('selectedpartners', views.selected, name='selectedpartners')
]
