from django.shortcuts import render


def team(request):
    """Team page view"""
    return render(request, 'team/team.html')
