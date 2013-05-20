# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
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
    
    _is_ajax = request.is_ajax()
    
    profile = get_object_or_404(Profile, id=int(profile_id))
    if request.POST:
        form = ProfileEditForm(data=request.POST, files=request.FILES, instance=profile)
        
        _is_valid = form.is_valid()
        if _is_valid:
            form.save()
        
        if not _is_ajax and _is_valid:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', \
                                            reverse('profile_edit', kwargs={'profile_id': profile.id })))

        if _is_ajax:
            return render(request, 'profile_edit_errors.html', {'form': form})

    else:
        form = ProfileEditForm(instance=profile)
        
    return render(request, 'profile_edit.html', {'form': form})


def request_log(request):
    request_logs = RequestLog.objects.order_by('id')[:10]
    request_logs = list(request_logs)
    
    return render(request, 'request_log.html', {'request_logs': request_logs})
