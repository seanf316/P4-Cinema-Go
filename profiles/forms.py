from django import forms
from djrichtextfield.widgets import RichTextWidget
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

        about = forms.CharField(widget=RichTextWidget())
