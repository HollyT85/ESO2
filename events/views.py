from django.shortcuts import render


def events(request):
    """Events page view"""
    return render(request, 'events/events.html')
