from django.test import TestCase
from .forms import UserForm, ProfileForm


class TestUserForm(TestCase):
    def test_userform_valid(self):
        """Test user form is valid"""
        form = UserForm(
            {
                "username": "testuser",
                "email": "testuser@test.com",
            }
        )
        self.assertTrue(form.is_valid())

    def test_userform_username_empty(self):
        """User form has empty username"""
        form = UserForm(
            {
                "username": "",
                "email": "testuser@test.com",
            }
        )
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors["username"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_userform_email_invalid(self):
        """User form passing email without "@"""
        form = UserForm(
            {
                "username": "testuser",
                "email": "testuser.test.com",
            }
        )
        self.assertIn("email", form.errors.keys())
        self.assertEqual(
            form.errors["email"][0], "Enter a valid email address."
        )
        self.assertFalse(form.is_valid())


class TestProfileForm(TestCase):
    def test_profileform_valid(self):
        """Test profile form is valid"""
        form = ProfileForm(
            {
                "firstname": "sean",
                "surname": "finn",
                "about": "I like movies",
                "profile_image": "test.jpg",
                "fav_movie": "Matrix",
                "fav_actor": "Denzel",
                "director": "John",
            }
        )
        self.assertTrue(form.is_valid())

    def test_profileform_invalid(self):
        """
        Test profile form is invalid due
        to field max lengths being exceeded
        """
        form = ProfileForm(
            {
                "firstname": str("a" * 51),
                "surname": str("a" * 51),
                "about": str("a" * 201),
                "profile_image": "test.jpg",
                "fav_movie": str("a" * 51),
                "fav_actor": str("a" * 51),
                "director": str("a" * 51),
            }
        )
        self.assertIn("firstname", form.errors.keys())
        self.assertIn("surname", form.errors.keys())
        self.assertIn("about", form.errors.keys())
        self.assertIn("fav_movie", form.errors.keys())
        self.assertIn("fav_actor", form.errors.keys())
        self.assertIn("director", form.errors.keys())
        self.assertEqual(
            form.errors["firstname"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["surname"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["about"][0],
            "Ensure this value has at most 200 characters (it has 201).",
        )
        self.assertEqual(
            form.errors["fav_movie"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["fav_actor"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["director"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertFalse(form.is_valid())
