from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Certification(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200)

class Director(models.Model):
    name = models.CharField(max_length=50)

class OTT(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    orginal_title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    certification = models.ManyToManyField(Certification)
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    otts =  models.ManyToManyField(OTT)
    video = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
