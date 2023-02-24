from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        help_texts = {
            "username": None,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "firstname",
            "surname",
            "about",
            "profile_image",
            "fav_movie",
            "director",
        ]

        widgets = {"about": SummernoteWidget()}
