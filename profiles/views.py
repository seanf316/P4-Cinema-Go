from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm, UserForm


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
    }

    return render(request, "profiles/profile.html", context)


def edit_profile(request, username):

    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        edit_user = UserForm(request.POST, instance=request.user)
        edit_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if edit_user.is_valid() and edit_form.is_valid():
            edit_user.save()
            edit_form.save()
            messages.success(request, "Your Profile has been updated!")
            return redirect(reverse("profile", args=[username]))
    else:
        edit_user = UserForm(instance=request.user)
        edit_form = ProfileForm(instance=request.user.profile)

    context = {
        "profile": profile,
        "edit_user": edit_user,
        "edit_form": edit_form,
    }

    return render(request, "profiles/edit_profile.html", context)
