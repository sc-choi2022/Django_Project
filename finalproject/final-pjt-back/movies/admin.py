from django.contrib import admin
from .models import Movie, Genre, Certification, Actor, Director, OTT, Keyword, Review

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Certification)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(OTT)
admin.site.register(Keyword)
admin.site.register(Review)