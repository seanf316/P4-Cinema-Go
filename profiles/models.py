from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from movie.models import Movie

placeholder = "https://res.cloudinary.com/seanf316/image/upload/v1677195145/Cinema-Go/default_profile_llyxo2.webp"


class Profile(models.Model):
    """
    Model for creating a Profile
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, related_name="profile"
    )
    firstname = models.CharField(
        max_length=50, null=True, blank=True, default="Firstname"
    )
    surname = models.CharField(
        max_length=50, null=True, blank=True, default="Surname"
    )
    about = models.TextField(
        max_length=200, null=True, blank=True, default="I love Cinema|Go"
    )
    profile_image = CloudinaryField(
        "image",
        default=placeholder,
        eager=[{"width": "50", "height": "50", "crop": "crop"}],
        transformation={
            "width": "600",
            "height": "600",
            "crop": "fill",
        },
        folder="/images",
        format="webp",
    )
    fav_movie = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="What's your favourite Movie?",
    )
    director = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Who's your favourite Director?",
    )
    to_watch = models.ManyToManyField(
        Movie, related_name="to_watch", blank=True
    )
    reviewed = models.ManyToManyField(
        Movie, related_name="reviewed", blank=True
    )

    def __str__(self):
        """
        Returns the username of the profile as a string representation of
        the object.
        """
        return str(self.user)
