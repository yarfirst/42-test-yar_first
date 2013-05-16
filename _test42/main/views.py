# Create your views here.
from django.shortcuts import render, get_object_or_404

from models import Profile, RequestLog


def profile(request):
    profile = get_object_or_404(Profile, id=1)

    request_logs = RequestLog.objects.order_by('id')[:10]
    request_logs = list(request_logs)
    return render(request, 'profile.html', {
                    'profile': profile,
                    'request_logs': request_logs
                })
