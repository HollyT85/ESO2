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

def fossilfest(request):
    """Events page view"""
    return render(request, 'events/fossilfest.html')

def staithes(request):
    """Events page view"""
    return render(request, 'events/staithes.html')

def redcar(request):
    """Events page view"""
    return render(request, 'events/redcar.html')