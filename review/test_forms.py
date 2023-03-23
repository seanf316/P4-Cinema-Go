from django.test import TestCase
from .forms import ReviewForm, CommentForm


class TestReviewForm(TestCase):
    def test_reviewform_valid(self):
        """Test review form is valid"""
        form = ReviewForm(
            {
                "review": "This is a good movie",
                "rating": 8,
            }
        )
        self.assertTrue(form.is_valid())

    def test_reviewform_review_empty(self):
        """Review form has empty review"""
        form = ReviewForm(
            {
                "review": "",
                "rating": 8,
            }
        )
        self.assertIn("review", form.errors.keys())
        self.assertEqual(form.errors["review"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_reviewform_review_above_max_characters(self):
        """Review form review field exceeds 2500 characters"""
        form = ReviewForm(
            {
                "review": str("a" * 6000),
                "rating": 8,
            }
        )
        self.assertIn("review", form.errors.keys())
        self.assertEqual(
            form.errors["review"][0],
            "Ensure this value has at most 2500 characters (it has 6000).",
        )
        self.assertFalse(form.is_valid())

    def test_reviewform_rating_below_min(self):
        """Review form has rating below 1"""
        form = ReviewForm(
            {
                "review": "Good",
                "rating": 0,
            }
        )
        self.assertIn("rating", form.errors.keys())
        self.assertEqual(
            form.errors["rating"][0],
            "Ensure this value is greater than or equal to 1.",
        )
        self.assertFalse(form.is_valid())

    def test_reviewform_rating_above_max(self):
        """Review form has rating above 10"""
        form = ReviewForm(
            {
                "review": "Good",
                "rating": 11,
            }
        )
        self.assertIn("rating", form.errors.keys())
        self.assertEqual(
            form.errors["rating"][0],
            "Ensure this value is less than or equal to 10.",
        )
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    def test_commentform_valid(self):
        """Test comment form is valid"""
        form = CommentForm({"body": "This is a good movie"})
        self.assertTrue(form.is_valid())

    def test_commentform_body_empty(self):
        """Comment form has empty body"""
        form = CommentForm({"body": ""})
        self.assertIn("body", form.errors.keys())
        self.assertEqual(form.errors["body"][0], "This field is required.")
        self.assertFalse(form.is_valid())

    def test_commentform_body_above_max_characters(self):
        """Comment form body field exceeds 500 characters"""
        form = CommentForm({"body": str("a" * 600)})
        self.assertIn("body", form.errors.keys())
        self.assertEqual(
            form.errors["body"][0],
            "Ensure this value has at most 500 characters (it has 600).",
        )
        self.assertFalse(form.is_valid())
