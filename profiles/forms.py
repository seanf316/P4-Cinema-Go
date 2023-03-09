from django import forms
from djrichtextfield.widgets import RichTextWidget
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    """
    Form to Edit User-Username
    """

    class Meta:
        """
        Define model, form fields
        """

        model = User
        fields = ["username"]
        help_texts = {
            "username": None,
        }


class ProfileForm(forms.ModelForm):
    """
    Form to Edit/Delete Profile
    Deleting Profile deletes User
    """

    class Meta:
        """
        Define model, form fields, labels and widgets
        """

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
