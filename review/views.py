import os
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from django.contrib.auth.models import User
from movie.models import Movie
from profiles.models import Profile
from .forms import ReviewForm

API_KEY = os.environ.get("API_KEY")


@login_required()
def review(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"

    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

    movie = Movie.objects.get(MovieId=movie_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    if Review.objects.filter(movie=movie, user=user).exists():
        review_exists = True
    else:
        review_exists = False

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.movie = movie
            profile.reviewed.add(movie)
            review.save()
            messages.success(
                request, f"{user.username} you have reviewed {movie}"
            )

            return redirect(reverse("moviedetails", args=[movie_id]))

    else:
        form = ReviewForm()

    context = {
        "form": form,
        "movie": movie,
        "review_exists": review_exists,
        "movie_data": movie_data,
        "hero": hero,
    }

    return render(request, "review/review.html", context)


def edit_review(request, movie_id, review_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"

    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

    movie = Movie.objects.get(MovieId=movie_id)
    review = Review.objects.get(id=review_id)
    user = request.user

    if review.user != user:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect(reverse("review", args=[review.movie.MovieId]))

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            messages.success(
                request, f"{user.username} your review has been updated"
            )

            return redirect(reverse("moviedetails", args=[movie_id]))

    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
        "review": review,
        "movie": movie,
        "movie_data": movie_data,
        "hero": hero,
    }

    return render(request, "review/review.html", context)
