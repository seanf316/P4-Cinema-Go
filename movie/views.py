import os
from django.shortcuts import render
from django.template import loader
import requests

API_KEY = os.environ.get("API_KEY")


def trending(request):
    """
    Call on the TMDB API to provide some trending movies
    """
    url = (
        "https://api.themoviedb.org/3/trending/movie/day?api_key="
        + API_KEY
        + "&language=en-US&page=1"
    )

    response = requests.get(url)
    movie_data = response.json()

    context = {
        "movie_data": movie_data,
        "page_number": 2,
    }

    return render(request, "movie/trending.html", context)


def pagination(request, page_number):
    url = (
        "https://api.themoviedb.org/3/trending/movie/day?api_key="
        + API_KEY
        + "&language=en-US&page="
        + str(page_number)
    )

    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) + 1

    context = {
        "movie_data": movie_data,
        "page_number": page_number,
    }

    return render(request, "movie/trending.html", context)
