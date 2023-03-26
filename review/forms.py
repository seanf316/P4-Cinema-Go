from django import forms
from djrichtextfield.widgets import RichTextWidget
from review.models import Review, Comment


class ReviewForm(forms.ModelForm):
    """
    Form to Edit/Delete Review
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Review
        fields = [
            "review",
            "rating",
        ]
        labels = {
            "review": "Review (Max 2500 Characters)",
            "rating": "Rating (1-10)",
        }

        review = forms.CharField(widget=RichTextWidget())


class CommentForm(forms.ModelForm):
    """
    Form to Edit/Delete Review
    """

    class Meta:
        """
        Define model, form fields and widgets
        """

        model = Comment
        fields = ("body",)

        labels = {
            "body": "Comment (Max 500 Characters)",
        }

        review = forms.CharField(widget=RichTextWidget())
