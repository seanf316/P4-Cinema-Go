from django.test import TestCase


class TestViews(TestCase):
    """
    Test Home Views
    """

    def test_home_page(self):
        """
        Test Home Views
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
