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

        labels = {
            "firstname": "First Name",
            "surname": "Last Name",
            "about": "About Me",
            "profile_image": "Profile Image",
            "fav_movie": "Favorite Movie",
            "director": "Favorite Director",
        }

        about = forms.CharField(widget=RichTextWidget())
