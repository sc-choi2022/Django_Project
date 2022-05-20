from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    users_mymovie = models.ManyToManyField(Movie, related_name='movies_mymovie')
    users_wish = models.ManyToManyField(Movie, related_name='movies_wish')