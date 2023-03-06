# Code created following this video - https://youtu.be/FdVuKt_iuSI
# Expectation Profile is automatically created when User sign's up

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    When a user signs up to a site they will automatically
    create a Profile
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Any changes made to User account is saved to Profile
    """
    instance.profile.save()
