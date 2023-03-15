from django.urls import path
from . import views

urlpatterns = [
    path(
        "review/<int:movie_id>/",
        views.review,
        name="review",
    ),
    path(
        "review/<int:movie_id>/<int:review_id>/",
        views.edit_review,
        name="edit_review",
    ),
    path(
        "review/<int:movie_id>/<int:review_id>/delete/",
        views.delete_review,
        name="delete_review",
    ),
    path(
        "comment/<int:movie_id>/<int:review_id>/",
        views.comment,
        name="comment",
    ),
    path(
        "comment/<int:movie_id>/<int:review_id>/comments/<int:comment_id>/edit/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "allreviews/",
        views.allreviews,
        name="allreviews",
    ),
]
