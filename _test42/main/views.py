# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from models import Profile, RequestLog
from forms import ProfileEditForm

def profile(request):
    profile = Profile.objects.all()[0]

    return render(request, 'profile.html', {'profile': profile})


@login_required
def profile_edit(request, profile_id=None):
    if not profile_id or not profile_id.isdigit():
        raise Http404
    
    profile = get_object_or_404(Profile, id=int(profile_id))
    if request.POST:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileEditForm(instance=profile)
        
    return render(request, 'profile_edit.html', {'form': form})


def request_log(request):
    request_logs = RequestLog.objects.order_by('id')[:10]
    request_logs = list(request_logs)
    
    return render(request, 'request_log.html', {'request_logs': request_logs})
