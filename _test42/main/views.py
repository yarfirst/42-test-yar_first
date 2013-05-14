# Create your views here.
from django.shortcuts import render, get_object_or_404

from models import Profile


def profile(request):
    profile = get_object_or_404(Profile, pk=1)
    return render(request, 'profile.html', {'pofile': profile})
    
