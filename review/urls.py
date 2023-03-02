from django.urls import path
from . import views

urlpatterns = [
    path(
        "review/<int:movie_id>/",
        views.review,
        name="review",
    ),
]
