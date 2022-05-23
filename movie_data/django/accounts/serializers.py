from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_articles', 'movies', 'users_mymovie', '')


class MovieProfileSerializer(serializers.ModelSerializer):

    class ProfileSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)

    users_mymovie = ProfileSerializer(read_only=True, many=True)
    users_wish = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('users_mymovie', 'users_wish', 'username',)










        # 'users_mymovie', 'users_wish'


    # class ArticleSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Article
    #         fields = ('pk', 'title',)

    # like_articles = ArticleSerializer(many=True)