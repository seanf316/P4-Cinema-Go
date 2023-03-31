import os
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, Comment
from django.contrib.auth.models import User
from movie.models import Movie
from profiles.models import Profile
from .forms import ReviewForm, CommentForm

API_KEY = os.environ.get("API_KEY")


@login_required()
def review(request, movie_id):
    """
    At the movie details page this function checks if a review for
    the current selected movie exists, if it does not the user can click the
    review button and the review page will be rendered containing the review
    form. If review is made the review will be rendered on the movie details
    page and also saved to the database for reference later
    """
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        f"&language=en-US&append_to_response=credits,videos,images"
    )
    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = (
            "https://res.cloudinary.com/seanf316/image/"
            f"upload/v1680055493/background_r1z21m.webp"
        )

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

            return redirect(reverse("allreviews"))
        else:
            messages.success(
                request,
                "Review field cannot be blank or exceed 2500 characters.",
            )
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
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        f"&language=en-US&append_to_response=credits,videos,images"
    )

    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = (
            "https://res.cloudinary.com/seanf316/image/"
            f"upload/v1680055493/background_r1z21m.webp"
        )

    movie = Movie.objects.get(MovieId=movie_id)
    review = Review.objects.get(id=review_id)
    user = request.user

    if review.user != user:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect(reverse("allreviews"))

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            messages.success(
                request, f"{user.username} your review has been updated"
            )

            return redirect(reverse("allreviews"))
        else:
            messages.success(
                request,
                "Review field cannot be blank or exceed 2500 characters.",
            )
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
        return redirect(reverse("allreviews"))

    profile = Profile.objects.get(user=user)
    if review.movie in profile.reviewed.all():
        profile.reviewed.remove(review.movie)

    review.delete()
    messages.success(request, f"{user.username} your review has been deleted")

    return redirect(reverse("allreviews"))


@login_required()
def allreviews(request):
    """
    Function to render all reviews to the review page, also queries database to
    see if the reviews have comments
    """
    reviews = Review.objects.all()

    review_content = []
    for review in reviews:
        user = request.user
        profile = Profile.objects.get(user=user)
        movie = review.movie
        movie_id = movie.MovieId
        comments = Comment.objects.filter(
            review=review,
        ).order_by("created_on")

        url = (
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
            f"&language=en-US&append_to_response=credits,videos,images"
        )
        response = requests.get(url)
        movie_data = response.json()
        backdrop = movie_data["backdrop_path"]
        if backdrop:
            hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
        else:
            hero = (
                "https://res.cloudinary.com/seanf316/image/"
                f"upload/v1680055493/background_r1z21m.webp"
            )

        review_content.append(
            {"movie_data": movie_data, "hero": hero, "review": review}
        )

    context = {
        "review_content": review_content,
    }

    return render(request, "review/allreviews.html", context)


@login_required()
def comment(request, movie_id, review_id):
    """
    Function to comment on existing reviews
    """
    movie = Movie.objects.get(MovieId=movie_id)
    review = Review.objects.get(id=review_id)
    movie_id = movie.MovieId

    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        f"&language=en-US&append_to_response=credits,videos,images"
    )
    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = (
            "https://res.cloudinary.com/seanf316/image/"
            f"upload/v1680055493/background_r1z21m.webp"
        )

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.name = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect(reverse("allreviews"))
        else:
            messages.success(
                request,
                "Comment field cannot be blank or exceed 500 characters.",
            )
    else:
        form = CommentForm()

    context = {
        "form": form,
        "movie": movie,
        "movie_data": movie_data,
        "hero": hero,
        "review": review,
    }

    return render(request, "review/comment.html", context)


@login_required()
def edit_comment(request, movie_id, review_id, comment_id):
    """
    Function to edit comment
    """
    movie = Movie.objects.get(MovieId=movie_id)
    review = Review.objects.get(id=review_id)
    movie_id = movie.MovieId
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        f"&language=en-US&append_to_response=credits,videos,images"
    )
    response = requests.get(url)
    movie_data = response.json()
    backdrop = movie_data["backdrop_path"]
    if backdrop:
        hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
    else:
        hero = (
            "https://res.cloudinary.com/seanf316/image/"
            f"upload/v1680055493/background_r1z21m.webp"
        )

    if comment.name != user:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect(reverse("allreviews"))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            messages.success(
                request, f"{user.username} your comment has been updated."
            )
            return redirect(reverse("allreviews"))
        else:
            messages.success(
                request,
                "Comment field cannot be blank or exceed 500 characters.",
            )
    else:
        form = CommentForm(instance=comment)

    context = {
        "form": form,
        "movie": movie,
        "movie_data": movie_data,
        "hero": hero,
        "review": review,
    }

    return render(request, "review/comment.html", context)


@login_required()
def delete_comment(request, movie_id, review_id, comment_id):
    """
    Function to delete comment
    """
    user = request.user
    comment = Comment.objects.get(id=comment_id)

    if comment.name != user:
        messages.error(
            request, "You are not authorized to delete this comment."
        )
        return redirect(reverse("allreviews"))

    comment.delete()
    messages.success(
        request, f"{user.username} your comment has been deleted."
    )

    return redirect(reverse("allreviews"))
