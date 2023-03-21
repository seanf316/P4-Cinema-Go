from django.test import TestCase
from django.contrib.auth.models import User
from movie.models import Movie
from .models import Profile


class TestProfileModel(TestCase):
    """
    Testing Profile Model
    """

    def setUp(self):
        """
        Sets the Profile Object with required attributes
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
        self.profile = Profile.objects.get(user=self.user)
        self.profile.firstname = "Sean"
        self.profile.surname = "Finn"
        self.profile.about = "I like movies"
        self.profile.profile_image = "test.jpg"
        self.profile.fav_movie = "Matrix"
        self.profile.fav_actor = "Denzel"
        self.profile.director = "John"
        self.profile.to_watch.add(self.movie)
        self.profile.reviewed.add(self.movie)
        self.expected_str = str(self.user)

    def test_profile_model(self):
        """
        Tests the Profile model's attributes
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.firstname, "Sean")
        self.assertEqual(self.profile.surname, "Finn")
        self.assertEqual(self.profile.about, "I like movies")
        self.assertEqual(self.profile.profile_image, "test.jpg")
        self.assertEqual(self.profile.fav_movie, "Matrix")
        self.assertEqual(self.profile.fav_actor, "Denzel")
        self.assertEqual(self.profile.director, "John")
        self.assertEqual(str(self.profile), self.expected_str)
