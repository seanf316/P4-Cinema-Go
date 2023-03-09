from django import forms
from djrichtextfield.widgets import RichTextWidget
from review.models import Review


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

    review = forms.CharField(widget=RichTextWidget())
