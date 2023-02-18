from django.urls import path
from . import views

urlpatterns = [
    path(
        "trending/",
        views.movies,
        {"category": "trending"},
        name="trending",
    ),
    path(
        "toprated/",
        views.movies,
        {"category": "toprated"},
        name="toprated",
    ),
    path(
        "pagination/<int:page_number>/<str:category>/",
        views.pagination,
        name="pagination",
    ),
    path(
        "moviedetails/<int:movie_id>", views.moviedetails, name="moviedetails"
    ),
]
