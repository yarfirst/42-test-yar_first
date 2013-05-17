# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from models import Profile, RequestLog


def profile(request):
    profile = Profile.objects.all()[0]

    return render(request, 'profile.html', {'profile': profile})


@login_required
def profile_edit(request):
    pass


def request_log(request):
    request_logs = RequestLog.objects.order_by('id')[:10]
    request_logs = list(request_logs)
    
    return render(request, 'request_log.html', {'request_logs': request_logs})
