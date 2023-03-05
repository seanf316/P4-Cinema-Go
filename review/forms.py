from django import forms
from djrichtextfield.widgets import RichTextWidget
from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "review",
            "rating",
        ]

    review = forms.CharField(widget=RichTextWidget())
