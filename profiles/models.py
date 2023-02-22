from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

placeholder = "https://res.cloudinary.com/seanf316/image/upload/v1677023649/default-profile_fb2lrf_xbtzxc.jpg"


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, related_name="profile"
    )
    firstname = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=200, null=True, blank=True)
    profile_image = CloudinaryField("image", default=placeholder)

    def __str__(self):
        return str(self.user)
