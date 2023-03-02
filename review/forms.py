from django import forms
from django_summernote.widgets import SummernoteWidget
from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "review",
            "rating",
        ]

        widgets = {"review": SummernoteWidget()}
