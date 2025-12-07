from django.shortcuts import render


def partners(request):
    """Partners page view"""
    return render(request, 'partners/partners.html')
