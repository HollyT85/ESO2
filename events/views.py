from django.shortcuts import render


def events(request):
    """Events page view"""
    return render(request, 'events/events.html')

def upcoming(request):
    """Events page view"""
    return render(request, 'events/upcoming.html')

def previous(request):
    """Events page view"""
    return render(request, 'events/previous.html')