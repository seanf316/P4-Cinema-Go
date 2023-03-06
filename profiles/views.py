from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from movie.models import Movie
from .forms import ProfileForm, UserForm


@login_required()
def profile(request, username):
    """
    Renders the users profile, checks that the user matches profile user
    """
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
    }

    return render(request, "profiles/profile.html", context)


@login_required()
def edit_profile(request, username):
    """
    Renders the edit profile page, checks that the user matches profile user
    and whether the forms are valid before saving to database
    """
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
            messages.success(
                request, f"{user.username} your profile has been updated!"
            )
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


@login_required()
def delete_profile(request, username):
    """
    Querys the database for the User that matches profile user
    and deletes user & profile
    """
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(
            request, "Sorry to see you go, your Account has been deleted."
        )
        return redirect(reverse("home"))

    context = {"username": username}
    return render(request, "profiles/edit_profile.html", context)
