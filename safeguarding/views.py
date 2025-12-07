from django.shortcuts import render


def safeguarding(request):
    """Safeguarding page view"""
    return render(request, 'safeguarding/safeguarding.html')
