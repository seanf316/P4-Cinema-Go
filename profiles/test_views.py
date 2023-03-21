from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestProfileViews(TestCase):
    """
    Testing Movie Views
    """

    def setUp(self):
        """
        Setup creates user, profile and logs user in
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testpass"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.client.login(username="testuser", password="testpass")

    def test_profile_page_renders(self):
        """
        Test that profile view renders correct page
        """
        response = self.client.get(reverse("profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_edit_profile_page(self):
        """
        Test that edit profile view renders correct page and username updates
        correctly
        """
        response = self.client.get(reverse("edit_profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/edit_profile.html")
        new_username = "John"

        data = {
            "username": new_username,
        }
        response = self.client.post(
            reverse("edit_profile", args=[self.user.username]), data=data
        )
        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.username, new_username)

    def test_delete_profile(self):
        """
        Test that delete profile view renders correct page
        and user is deleted successfully
        """
        response = self.client.get(reverse("edit_profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/edit_profile.html")
        response = self.client.post(
            reverse("delete_profile", args=["testuser"])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(User.objects.filter(username="testuser").exists())
