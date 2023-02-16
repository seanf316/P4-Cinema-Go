from django.urls import path
from . import views

urlpatterns = [
    path("trending/<str:url>/", views.trending, name="trending"),
    path("trending/page/<page_number>/", views.pagination, name="pagination"),
    path("toprated/", views.toprated, name="toprated"),
]
