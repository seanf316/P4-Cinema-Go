from django.urls import path
from . import views

urlpatterns = [
    path(
        "search/",
        views.search,
        name="search",
    ),
    path(
        "searchresults/<str:query>/",
        views.searchresults,
        name="searchresults",
    ),
    path(
        "searchresults/<str:query>/<int:page_number>/",
        views.searchresults,
        name="searchresults_page",
    ),
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
