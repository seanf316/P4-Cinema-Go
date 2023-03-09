from django.db import models


class Movie(models.Model):
    """
    Model for creating a Movie
    """

    Name = models.CharField(max_length=100, null=True, blank=True)
    Overview = models.TextField(null=True, blank=True)
    Director = models.CharField(max_length=50, null=True, blank=True)
    Released = models.CharField(max_length=25, null=True, blank=True)
    Runtime = models.CharField(max_length=25, null=True, blank=True)
    MovieId = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        """
        Order set to the name attribute
        """

        ordering = ["Name"]

    def __str__(self):
        """
        Returns the name of the movie as a string representation of the object.
        """
        return self.Name
