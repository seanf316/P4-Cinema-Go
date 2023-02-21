from django.db import models


class Movie(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Overview = models.TextField(blank=True)
    Director = models.CharField(max_length=50, blank=True)
    Released = models.CharField(max_length=25, blank=True)
    Runtime = models.CharField(max_length=25, blank=True)
    MovieId = models.CharField(max_length=25, blank=True)

    class Meta:
        ordering = ["Name"]

    def __str__(self):
        return self.Name
