from django.contrib import admin
from .models import Category, Movie, MovieShots, RatingStar, Rating, Actor, Genre, Review

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Review)
