import os
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
import requests
from .models import Movie

API_KEY = os.environ.get("API_KEY")


def search(request):
    query = request.GET.get("query")

    if query:
        print(query)
        return redirect("searchresults", query=query)

    return render(request, "movie/search.html")


def searchresults(request, query, page_number=1):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={query}&page={page_number}"

    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) + 1

    context = {
        "query": query,
        "movie_data": movie_data,
        "page_number": page_number,
    }

    return render(request, "movie/searchresults.html", context)


def movies(request, category):
    """
    Call on the TMDB API to provide some movies based on the category
    """
    if category == "trending":
        url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}&language=en-US&page=1"
        template_name = "movie/trending.html"
    elif category == "toprated":
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1"
        template_name = "movie/toprated.html"
    else:
        # handle other categories
        pass

    response = requests.get(url)
    movie_data = response.json()

    context = {
        "movie_data": movie_data,
        "page_number": 2,
    }

    return render(request, template_name, context)


def pagination(request, page_number, category):

    if category == "trending":
        url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}&language=en-US&page={page_number}"
        template_name = "movie/trending.html"
    elif category == "toprated":
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page={page_number}"
        template_name = "movie/toprated.html"
    else:
        # handle other categories
        pass

    response = requests.get(url)
    movie_data = response.json()
    page_number = int(page_number) + 1

    context = {
        "movie_data": movie_data,
        "page_number": page_number,
    }

    return render(request, template_name, context)


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

    Movie.objects.get_or_create(
        Name=movie_data["original_title"],
        Overview=movie_data["overview"],
        Director=director_name,
        Released=movie_data["release_date"],
        Runtime=movie_data["runtime"],
        MovieId=movie_data["id"],
    )

    context = {
        "movie_data": movie_data,
        "hero": hero,
        "director_name": director_name,
        "trailer": trailer_key,
    }

    return render(request, "movie/moviedetails.html", context)
