from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id','title','poster_path')

    movies_mymovie = MovieSerializer(many=True, read_only=True)
    movies_wish = MovieSerializer(many=True, read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ('id','title',)

    like_articles = ArticleSerializer(many=True, read_only=True)  
    class Meta:
        model = User
        fields = ('id', 'username', 'movies_mymovie', 'movies_wish', 'like_articles',)
