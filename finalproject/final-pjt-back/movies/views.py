from django.shortcuts import get_object_or_404
from movies.models import Movie, Review
from movies.serializers import MovieMainListSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

@api_view(['GET'])
def index(request):
    keyword_list = ['2343', '9840', '180547', '18035', '12565','4344']
    keyword = random.choice(keyword_list)
    movies = Movie.objects.filter(keywords=keyword).order_by('?')[:10]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def my_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.users_mymovie.filter(pk=user.pk).exists():
        movie.users_mymovie.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.users_mymovie.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def wish(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.users_wish.filter(pk=user.pk).exists():
        movie.users_wish.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.users_wish.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def recommend_otts(request, ott_id):
    movies = Movie.objects.filter(otts=str(ott_id)).order_by('?')[:5]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def recommend_directors(request, director_id):
    movies = Movie.objects.filter(directors=str(director_id)).order_by('?')[:5]  
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def recommend_keywords(request, keyword_id):
    movies = Movie.objects.filter(keywords=str(keyword_id)).order_by('?')[:5]
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_detail(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)