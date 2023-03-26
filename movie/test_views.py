import os
from django.test import TestCase, Client
from django.urls import reverse
import requests
from django.contrib.auth.models import User
from profiles.models import Profile
from review.models import Review
from .models import Movie

API_KEY = os.environ.get("API_KEY")


class TestMovieViews(TestCase):
    """
    Testing Movie Views
    """

    def setUp(self):
        """
        Setup creates user, profile, movie and review.
        Movie is added to the profiles watchlist and review list
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.movie = Movie.objects.create(
            Name="Test Movie",
            Overview="Movie about testing.",
            Director="Tester",
            Released="2023",
            Runtime="90",
            MovieId="1",
        )
        self.review = Review.objects.create(
            user=self.user,
            movie=self.movie,
        )
        self.profile.to_watch.add(self.movie)
        self.profile.reviewed.add(self.movie)

    def test_search_page_and_search_results_page(self):
        """
        Test that search page renders and when query is passed page redirects
        to search results page
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie/search.html")
        query = "Batman"
        response = self.client.get(reverse("search") + "?query=" + query)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("searchresults", kwargs={"query": query})
        )
        response = self.client.get(
            reverse("searchresults", kwargs={"query": query})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie/searchresults.html")

    def test_trending_movies(self):
        """
        Tests that trending page renders
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("trending"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie/trending.html")

    def test_toprated_movies(self):
        """
        Tests that toprated page renders
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("toprated"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie/toprated.html")

    def test_movie_pagination(self):
        """
        Tests that pagination works on trending & toprated page
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse(
                "pagination", kwargs={"category": "trending", "page_number": 2}
            )
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            reverse(
                "pagination", kwargs={"category": "toprated", "page_number": 2}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_movie_details(self):
        """
        Tests movie details page renders
        Tests API call to TMDB(using id that contains a background image),
        Creates a new movie using the API data
        Adds the new movie to profile watchlist
        Creates review of the new movie and queries the database for reviews/user reviews
        """
        self.client.login(username="testuser", password="testpass")
        movie_id = "804150"
        api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"
        response = requests.get(api_url)
        movie_data = response.json()
        backdrop = movie_data["backdrop_path"]
        if backdrop:
            hero = "https://image.tmdb.org/t/p/w1280/" + backdrop
        else:
            hero = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

        self.assertEqual(hero, "https://image.tmdb.org/t/p/w1280/" + backdrop)

        movie_id_no_backdrop = "1033965"
        api_url_no_backdrop = f"https://api.themoviedb.org/3/movie/{movie_id_no_backdrop}?api_key={API_KEY}&language=en-US&append_to_response=credits,videos,images"
        response_no_backdrop = requests.get(api_url_no_backdrop)
        movie_data_no_backdrop = response_no_backdrop.json()
        backdrop_no_backdrop = movie_data_no_backdrop["backdrop_path"]
        if backdrop_no_backdrop:
            hero_no_backdrop = (
                "https://image.tmdb.org/t/p/w1280/" + _no_backdrop
            )
        else:
            hero_no_backdrop = "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg"

        self.assertEqual(
            hero_no_backdrop,
            "https://res.cloudinary.com/seanf316/image/upload/v1676857549/wp8923971_qd2bfr.jpg",
        )

        director = None
        for person in movie_data["credits"]["crew"]:
            if person["job"] == "Director":
                director = person
                break

        director_name = director["name"] if director is not None else None

        Movie.objects.get_or_create(
            Name=movie_data["original_title"],
            Overview=movie_data["overview"],
            Director=director_name,
            Released=movie_data["release_date"],
            Runtime=movie_data["runtime"],
            MovieId=movie_data["id"],
        )

        new_movie = Movie.objects.get(MovieId=movie_data["id"])

        Review.objects.create(user=self.user, movie=new_movie)

        user_review = Review.objects.filter(user=self.user, movie=new_movie)
        if user_review.exists():
            user_review_exists = True
        else:
            user_review_exists = False
        self.assertTrue(user_review_exists)

        reviews = Review.objects.filter(movie=self.movie)
        if reviews.exists():
            review_exists = True
        else:
            review_exists = False
        self.assertTrue(review_exists)

        self.profile.to_watch.add(new_movie)
        if self.profile.to_watch.filter(MovieId=new_movie.MovieId).exists():
            to_watch = True
        else:
            to_watch = False
        self.assertTrue(to_watch)

        Review.objects.all().delete()
        if user_review.exists():
            user_review_exists = True
        else:
            user_review_exists = False
        self.assertFalse(user_review_exists)

        if reviews.exists():
            review_exists = True
        else:
            review_exists = False
        self.assertFalse(review_exists)

        self.profile.to_watch.clear()
        if self.profile.to_watch.filter(MovieId=new_movie.MovieId).exists():
            to_watch = True
        else:
            to_watch = False
        self.assertFalse(to_watch)

        response = self.client.get(
            reverse("moviedetails", kwargs={"movie_id": movie_id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie/moviedetails.html")

    def test_add_movie_to_watchlist(self):
        """
        First test clears watchlist and then tests adding setup movie to watchlist
        """
        self.profile.to_watch.clear()
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("watchlist", kwargs={"movie_id": self.movie.MovieId})
        )
        self.assertEqual(response.status_code, 302)

    def test_remove_movie_from_to_watch_list(self):
        """
        Test to remove setup movie from watchlist
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("watchlist", kwargs={"movie_id": self.movie.MovieId})
        )
        self.assertFalse(self.movie in self.profile.to_watch.all())

    def test_remove_movie_from_profile_page_watchlist(self):
        """
        Test to remove setup movie from profile page watchlist
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("prof_watch", kwargs={"movie_id": self.movie.MovieId})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.movie in self.profile.to_watch.all())

    def test_manage_review_from_profile_page_reviewlist(self):
        """
        Test to manage review from profile page review list
        """
        self.client.login(username="testuser", password="testpass")
        review = Review.objects.get(user=self.user, movie=self.movie)

        if review:
            if self.movie in self.profile.reviewed.all():
                return reverse(
                    "edit_review", args=[self.movie.MovieId, review.id]
                )
