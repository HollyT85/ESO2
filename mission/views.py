from django.shortcuts import render


def mission(request):
    """Mission page view"""
    return render(request, 'mission/mission.html')
