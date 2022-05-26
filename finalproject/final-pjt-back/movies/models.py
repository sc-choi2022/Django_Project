from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    runtime = models.IntegerField()
    video = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    users_mymovie = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_mymovie')
    users_wish = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies_wish')

class Genre(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name='genres')

class Certification(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name='certifications')

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie, related_name='actors')

class Director(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name='directors')

class OTT(models.Model):
    name = models.CharField(max_length=50)
    movies =  models.ManyToManyField(Movie, related_name='otts')

class Keyword(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name='keywords')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(max_length=100)
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)