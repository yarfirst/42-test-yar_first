# Create your views here.
from django.shortcuts import render

from models import Profile, RequestLog


def profile(request):
    profile = Profile.objects.all()[0]

    return render(request, 'profile.html', {'profile': profile})


def request_log(request):
    request_logs = RequestLog.objects.order_by('id')[:10]
    request_logs = list(request_logs)
    
    return render(request, 'request_log.html', {'request_logs': request_logs})
