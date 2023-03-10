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
    """
    At the movie details page this function checks if a review for
    the current selected movie exists, if it does not the user can click the
    review button and the review page will be rendered containing the review form.
    If review is made the review will be rendered on the movie details page and also
    saved to the database for reference later
    """
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


@login_required()
def edit_review(request, movie_id, review_id):
    """
    Checks the database for the Review.id/Movieid and then confirms if
    user matches the review user before allowing user to edit their review
    """
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


@login_required()
def delete_review(request, movie_id, review_id):
    """
    Querys database for specific review based off id, checks if user
    matches review.user and then deletes the user if request is valid.
    Review will also be removed from Profile reviewed list
    """
    review = Review.objects.get(id=review_id)
    user = request.user

    if review.user != user:
        messages.error(
            request, "You are not authorized to delete this review."
        )
        return redirect(reverse("review", args=[review.movie.MovieId]))

    profile = Profile.objects.get(user=user)
    if review.movie in profile.reviewed.all():
        profile.reviewed.remove(review.movie)

    review.delete()
    messages.success(request, f"{user.username} your review has been deleted")

    return redirect(reverse("moviedetails", args=[movie_id]))


@login_required()
def allreviews(request):

    reviews = Review.objects.all()

    review_content = []
    for review in reviews:
        user = request.user
        profile = Profile.objects.get(user=user)
        movie = review.movie
        movie_id = movie.MovieId

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"

        response = requests.get(url)
        movie_data = response.json()
        backdrop = movie_data["backdrop_path"]
        if backdrop:
            hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
        else:
            hero = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

        review_content.append(
            {"movie_data": movie_data, "hero": hero, "review": review}
        )

    context = {
        "review_content": review_content,
    }

    return render(request, "review/allreviews.html", context)
