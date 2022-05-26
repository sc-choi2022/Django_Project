from rest_framework import serializers
from .models import Movie, Actor, Director, Genre, Certification, OTT, Keyword, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('id', 'name', 'profile_path',)
        
    actors = ActorSerializer(many=True, read_only=True)

    class DirectorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('id', 'name',)
        
    directors = DirectorSerializer(many=True, read_only=True)

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('id', 'name',)
        
    genres = GenreSerializer(many=True, read_only=True)

    class CertificationSerializer(serializers.ModelSerializer):

        class Meta:

            model = Certification
            fields = ('id', 'name',)

    certifications = CertificationSerializer(many=True, read_only=True)

    class OTTSerializer(serializers.ModelSerializer):

        class Meta:
            model = OTT
            fields = ('id', 'name',)
        
    otts = OTTSerializer(many=True, read_only=True)

    users_mymovie = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    users_wish = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
       
    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = '__all__'

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        exclude = ('original_title',)

class MovieMainListSerializer(serializers.ModelSerializer):

    class KeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Keyword
            fields = ('id', 'name',)
        
    keywords = KeywordSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'title', 'video', 'keywords',)

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('id', 'content', 'movie', 'created_at', 'updated_at', 'rank', 'user',)
        read_only_fields = ('movie',)