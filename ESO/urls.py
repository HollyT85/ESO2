"""
URL configuration for ESO project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('events/', include('events.urls')),
    path('mission/', include('mission.urls')),
    path('team/', include('team.urls')),
    path('partners/', include('partners.urls')),
    path('safeguarding/', include('safeguarding.urls')),
    path('contact/', include('contact.urls')),
]
