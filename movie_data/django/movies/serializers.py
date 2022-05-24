from rest_framework import serializers
from .models import Movie, Actor, Director, Genre, Certification, OTT, Keyword

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

    # vue로 내일 볼 것 안되면 class User 만들어서 바꿔줄 것
    users_mymovie = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    users_wish = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('original_title',)


# 원본
class MovieListSerializer(serializers.ModelSerializer):

    class OTTSerializer(serializers.ModelSerializer):

        class Meta:
            model = OTT
            fields = ('id', 'name',)
        
    otts = OTTSerializer(many=True, read_only=True)


    class DirectorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('id', 'name',)
        
    directors = DirectorSerializer(many=True, read_only=True)


    class KeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Keyword
            fields = ('id', 'name',)
        
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'title', 'video', 'otts', 'directors', 'keywords',)



class MovieMainListSerializer(serializers.ModelSerializer):


    class KeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Keyword
            fields = ('id', 'name',)
        
    keywords = KeywordSerializer(many=True, read_only=True)
    

    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'title', 'video', 'keywords',)
