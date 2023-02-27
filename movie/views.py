import os
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template import loader
from django.contrib import messages
import requests
from .models import Movie
from profiles.models import Profile

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
    page_number = int(page_number)
    prev_page = page_number - 1 if page_number > 1 else None
    next_page = (
        page_number + 1 if movie_data["total_pages"] > page_number else None
    )

    context = {
        "query": query,
        "movie_data": movie_data,
        "page_number": page_number,
        "prev_page": prev_page,
        "next_page": next_page,
    }

    return render(request, "movie/searchresults.html", context)


def movies(request, category, page_number=1):
    """
    Call on the TMDB API to provide some movies based on the category
    """
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
    page_number = int(page_number)
    prev_page = page_number - 1 if page_number > 1 else None
    next_page = (
        page_number + 1 if movie_data["total_pages"] > page_number else None
    )

    context = {
        "movie_data": movie_data,
        "page_number": page_number,
        "prev_page": prev_page,
        "next_page": next_page,
    }

    return render(request, template_name, context)


def pagination(request, category, page_number=1):

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
    page_number = int(page_number)
    prev_page = page_number - 1 if page_number > 1 else None
    next_page = page_number + 1

    context = {
        "movie_data": movie_data,
        "page_number": page_number,
        "prev_page": prev_page,
        "next_page": next_page,
    }

    return render(request, template_name, context)


def moviedetails(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"

    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

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

    movie = Movie.objects.get(MovieId=movie_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.to_watch.filter(MovieId=movie_id).exists():
        to_watch = True
    else:
        to_watch = False

    context = {
        "movie_data": movie_data,
        "hero": hero,
        "director_name": director_name,
        "trailer": trailer_key,
        "to_watch": to_watch,
    }

    return render(request, "movie/moviedetails.html", context)


def watchlist(request, movie_id):
    movie = Movie.objects.get(MovieId=movie_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if movie in profile.to_watch.all():
        profile.to_watch.remove(movie)
        messages.success(
            request,
            f"{user.username} you have removed {movie} from your watchlist",
        )
    else:
        profile.to_watch.add(movie)
        messages.success(
            request,
            f"{user.username} you have added {movie} to your watchlist",
        )
    return redirect("moviedetails", movie_id=movie_id)


def prof_watch(request, movie_id):
    movie = Movie.objects.get(MovieId=movie_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if movie in profile.to_watch.all():
        profile.to_watch.remove(movie)
        messages.success(
            request,
            f"{user.username} you have removed {movie} from your watchlist",
        )
    return redirect(reverse("profile", kwargs={"username": user.username}))
