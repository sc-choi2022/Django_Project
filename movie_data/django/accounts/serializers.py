from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id','title',)

    movies_mymovie = MovieSerializer(many=True, read_only=True)
    movies_wish = MovieSerializer(many=True, read_only=True)


    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ('id','title',)

    like_articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'movies_mymovie', 'movies_wish', 'like_articles',)
