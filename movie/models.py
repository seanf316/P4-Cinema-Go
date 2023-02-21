from django.db import models


class Movie(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Overview = models.TextField(null=True, blank=True)
    Director = models.CharField(max_length=50, null=True, blank=True)
    Released = models.CharField(max_length=25, null=True, blank=True)
    Runtime = models.CharField(max_length=25, null=True, blank=True)
    MovieId = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        ordering = ["Name"]

    def __str__(self):
        return self.Name
