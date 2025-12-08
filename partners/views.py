from django.shortcuts import render


def partners(request):
    """Partners page view"""
    return render(request, 'partners/partners.html')

def patrons(request):
    """Patrons page view"""
    return render(request, 'partners/patrons.html')

def sig(request):
    """Partners page view"""
    return render(request, 'partners/significantpartners.html')

def selected(request):
    """Partners page view"""
    return render(request, 'partners/selectedpartners.html')
