from django.shortcuts import render, get_object_or_404
import requests
from django.contrib.auth.models import User
from .models import Profile


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
    }

    return render(request, "profiles/profile.html", context)
