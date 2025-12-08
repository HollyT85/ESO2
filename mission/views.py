from django.shortcuts import render


def plan(request):
    """Mission page view"""
    return render(request, 'mission/plan.html')

def mission(request):
    """Mission page view"""
    return render(request, 'mission/mission.html')

def work(request):
    """Mission page view"""
    return render(request, 'mission/work.html')

"""Mission page view"""
    return render(request, 'mission/gallery.html')