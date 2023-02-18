import os
from django.shortcuts import render
from django.template import loader
import requests

API_KEY = os.environ.get("API_KEY")


def trending(request):
    """
    Call on the TMDB API to provide some trending movies
    """
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}&language=en-US&page=1"

    response = requests.get(url)
    movie_data = response.json()

    context = {
        "movie_data": movie_data,
        "page_number": 2,
    }

    return render(request, "movie/trending.html", context)


def toprated(request):
    """
    Call on the TMDB API to provide some trending movies
    """
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1"

    response = requests.get(url)
    movie_data = response.json()

    context = {
        "movie_data": movie_data,
        "page_number": 2,
    }

    return render(request, "movie/toprated.html", context)


def pagination(request, page_number):
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}&language=en-US&page=1{str(page_number)}"

    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) + 1

    context = {
        "movie_data": movie_data,
        "page_number": page_number,
    }

    return render(request, "movie/trending.html", context)


def moviedetails(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"

    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    hero = "https://image.tmdb.org/t/p/w1280/" + backdrop

    director = None
    for person in movie_data["credits"]["crew"]:
        if person["job"] == "Director":
            director = person
            break

    director_name = director["name"] if director is not None else None

    trailer = None
    for video in movie_data["videos"]["results"]:
        if video["type"] == "Trailer":
            trailer = video
            break

    trailer_key = trailer["key"] if trailer is not None else None

    context = {
        "movie_data": movie_data,
        "hero": hero,
        "director_name": director_name,
        "trailer": trailer_key,
    }

    return render(request, "movie/moviedetails.html", context)
