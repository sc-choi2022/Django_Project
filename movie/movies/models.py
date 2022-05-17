from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Releases(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    orginal_title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    releases = models.ManyToManyField(Releases)
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    video = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
