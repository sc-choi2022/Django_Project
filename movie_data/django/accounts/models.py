from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class Mymovie(models.Model):
    title = models.CharField(max_length=100)

class Wish(models.Model):
    title = models.CharField(max_length=100)

class User(AbstractUser):
    mymovies = models.ManyToManyField(Movie, related_name='users')
    wishes = models.ManyToManyField(Movie, related_name='users')