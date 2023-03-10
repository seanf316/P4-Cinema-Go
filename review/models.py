from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from movie.models import Movie


class Review(models.Model):
    """
    Model for creating a Review
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    review = RichTextField(max_length=2500, null=True, blank=True)
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    class Meta:
        """
        Order set to the created on attribute
        """

        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the User username and the Movie name as a string representation of the object.
        """
        return self.user.username + " - " + self.movie.Name
