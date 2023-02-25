from django.urls import path
from . import views

urlpatterns = [
    path(
        "profile/<username>/",
        views.profile,
        name="profile",
    ),
    path(
        "profile/<username>/edit_profile",
        views.edit_profile,
        name="edit_profile",
    ),
    path(
        "profile/<username>/delete",
        views.delete_profile,
        name="delete_profile",
    ),
]
