from django.shortcuts import render


def team(request):
    """Team page view"""
    return render(request, 'team/team.html')

def memoriam(request):
    """memoriam page view"""
    return render(request, 'team/memoriam.html')