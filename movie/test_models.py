from django.test import TestCase
from .models import Movie


class TestMovieModel(TestCase):
    """
    Testing Movie Model
    """

    def setUp(self):
        """
        Sets the Movie Object with required attributes
        """
        Movie.objects.create(
            Name="Test Movie",
            Overview="Movie about testing.",
            Director="Tester",
            Released="2023",
            Runtime="90",
            MovieId="1",
        )

    def test_movie_model(self):
        """
        Tests the Movie model's attributes
        """
        movie = Movie.objects.get(Name="Test Movie")
        self.assertEqual(movie.Name, "Test Movie")
        self.assertEqual(movie.Overview, "Movie about testing.")
        self.assertEqual(movie.Director, "Tester")
        self.assertEqual(movie.Released, "2023")
        self.assertEqual(movie.Runtime, "90")
        self.assertEqual(movie.MovieId, "1")
