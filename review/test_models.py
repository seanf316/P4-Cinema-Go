from django.test import TestCase
from django.contrib.auth.models import User
from movie.models import Movie
from .models import Review, Comment


class TestReviewModel(TestCase):
    """
    Testing Review Model
    """

    def setUp(self):
        """
        Sets the Review Object with required attributes
        """
        self.movie = Movie.objects.create(
            Name="Test Movie",
            Overview="Movie about testing.",
            Director="Tester",
            Released="2023",
            Runtime="90",
            MovieId="1",
        )
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.review = Review.objects.create(
            user=self.user,
            movie=self.movie,
            review="Good movie",
            rating=1,
        )
        self.expected_str = str(f"{self.user.username} - {self.movie.Name}")

    def test_review_model(self):
        """
        Tests the Review model's attributes
        """
        self.assertEqual(self.review.user.username, "testuser")
        self.assertEqual(self.review.movie.Name, "Test Movie")
        self.assertEqual(self.review.review, "Good movie")
        self.assertEqual(self.review.rating, 1)
        self.assertEqual(str(self.review), self.expected_str)


class TestCommentModel(TestCase):
    """
    Testing Comment Model
    """

    def setUp(self):
        """
        Sets the Comment Object with required attributes
        """
        self.movie = Movie.objects.create(
            Name="Test Movie",
            Overview="Movie about testing.",
            Director="Tester",
            Released="2023",
            Runtime="90",
            MovieId="1",
        )
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
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

        self.expected_str = str(f"Comment by {self.comment.name}")

    def test_comment_model(self):
        """
        Tests the Review model's attributes
        """
        self.assertEqual(self.comment.name.username, "testuser")
        self.assertEqual(self.comment.review, self.review)
        self.assertEqual(self.comment.body, "I agree")
        self.assertEqual(str(self.comment), self.expected_str)
