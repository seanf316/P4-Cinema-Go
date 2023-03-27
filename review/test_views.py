import os
from django.test import TestCase, Client
from django.urls import reverse
import requests
from django.contrib.auth.models import User
from movie.models import Movie
from profiles.models import Profile
from .models import Review, Comment

API_KEY = os.environ.get("API_KEY")


class TestReviewViews(TestCase):
    """
    Testing Review Views
    """

    def setUp(self):
        """
        Setup creates user, profile, movie and logs user in
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.profile = Profile.objects.get(user=self.user)
        movie_id = "804150"
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
                f"upload/v1676857549/wp8923971_qd2bfr.jpg"
            )

        director = None
        for person in movie_data["credits"]["crew"]:
            if person["job"] == "Director":
                director = person
                break

        director_name = director["name"] if director is not None else None

        self.movie = Movie.objects.create(
            Name=movie_data["original_title"],
            Overview=movie_data["overview"],
            Director=director_name,
            Released=movie_data["release_date"],
            Runtime=movie_data["runtime"],
            MovieId=movie_data["id"],
        )

        self.review = Review.objects.create(
            user=self.user,
            movie=self.movie,
            review="Good movie",
            rating=1,
        )

        self.comment = Comment.objects.create(
            review=self.review,
            name=self.user,
            body="I agree",
        )

        self.client.login(username="testuser", password="testpass")

    def test_review_page_and_reviewing(self):
        """
        Test that review view renders correct page with existing reviews
        and create review works
        """
        response = self.client.get(
            reverse("review", args={self.movie.MovieId})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review/review.html")

        review_data = {
            "review": "Brilliant love this movie",
            "rating": 10,
        }

        response = self.client.post(
            reverse("review", args={self.movie.MovieId}),
            data=review_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))

        new_review = Review.objects.get(id=2)
        self.assertEqual(new_review.review, "Brilliant love this movie")
        self.assertEqual(new_review.rating, 10)

    def test_edit_review(self):
        """
        Test editing a review
        """
        response = self.client.get(
            reverse(
                "edit_review",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review/review.html")

        self.assertEqual(self.review.review, "Good movie")
        self.assertEqual(self.review.rating, 1)

        review_data = {
            "review": "Cracking movie love this movie",
            "rating": 10,
        }

        response = self.client.post(
            reverse(
                "edit_review",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                },
            ),
            data=review_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))

        updated_review = Review.objects.get(id=self.review.id)
        self.assertEqual(
            updated_review.review, "Cracking movie love this movie"
        )
        self.assertEqual(updated_review.rating, 10)

    def test_delete_review(self):
        """
        Testing the delete review
        """
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        response = self.client.post(
            reverse(
                "delete_review",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())
        new_review_count = Review.objects.all().count()
        self.assertEqual(new_review_count, 0)

    def test_comment_on_review(self):
        """
        Test that comment shows and create a comment
        """
        response = self.client.get(
            reverse(
                "comment",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review/comment.html")

        comment_data = {
            "body": "This is a good review",
        }

        response = self.client.post(
            reverse(
                "comment",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                },
            ),
            data=comment_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))

        new_comment = Comment.objects.get(id=2)
        self.assertEqual(new_comment.body, "This is a good review")

    def test_edit_comment(self):
        """
        Test editing a comment
        """
        response = self.client.get(
            reverse(
                "edit_comment",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                    "comment_id": self.comment.id,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "review/comment.html")

        self.assertEqual(self.comment.body, "I agree")

        comment_data = {
            "body": "I do not agree!",
        }

        response = self.client.post(
            reverse(
                "edit_comment",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                    "comment_id": self.comment.id,
                },
            ),
            data=comment_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))

        updated_comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(updated_comment.body, "I do not agree!")

    def test_delete_comment(self):
        """
        Testing the delete comment
        """
        comment_count = Comment.objects.all().count()
        self.assertEqual(comment_count, 1)

        response = self.client.post(
            reverse(
                "delete_comment",
                kwargs={
                    "movie_id": self.movie.MovieId,
                    "review_id": self.review.id,
                    "comment_id": self.comment.id,
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("allreviews"))

        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
        new_comment_count = Comment.objects.all().count()
        self.assertEqual(new_comment_count, 0)
