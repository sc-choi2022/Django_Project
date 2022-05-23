import requests
from django.shortcuts import render, get_list_or_404, get_object_or_404
from movies.models import Movie, Genre, Certification, OTT, Keyword, Actor, Director
from dotenv import load_dotenv
import os
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import MovieMainListSerializer, MovieSerializer
load_dotenv()
API_KEY = os.environ.get('API_KEY')

order_certi = { 'ALL': 1, '12':2 , '15': 3, '18': 4}

def movie(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
        'page': 20,
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()['results']
    for d in data:
        id = d['id']
        path1 = '/movie/' + str(id)
        params1 = {
            'api_key': API_KEY,
            'language': 'ko',
            'append_to_response': 'releases',
        }
        response1 = requests.get(BASE_URL+path1, params=params1)
        data1 = response1.json()
        movie = Movie()
        movie.pk = id
        movie.title = data1['title']
        movie.orginal_title = data1['original_title']
        if data1['overview'] == '':
            continue
        movie.overview = data1['overview']
        movie.poster_path = data1['poster_path']
        if d['release_date'] == '':
            continue
        movie.release_date = data1['release_date']
        movie.runtime = data1['runtime']
        movie.vote_average = data1['vote_average']
        movie.vote_count = data1['vote_count']
        
        path2 = path1 + '/videos'
        params2 = {
            'api_key': API_KEY,
            'language': 'ko',
        }    
        response2 = requests.get(BASE_URL+path2, params=params2)  
        data2 = response2.json()['results']
        
        for d2 in data2:
            movie.video = ''
            if d2['type'] == 'Trailer' or d2['official'] == True:
                movie.video = d2['key']
                break
        if movie.video == '':
            continue
        movie.save()

        genres = data1['genres']
        for genre in genres:
            g1 = Genre(pk=genre['id'], name=genre['name'])
            g1.save()
            g1.movies.add(movie)

        certifi = data1['releases']['countries']
        for cer in certifi:
            if cer['iso_3166_1'] == 'KR' and cer['certification'] != '':
                if cer['certification'] == '전체관람가':
                    cer['certification'] = 'ALL'
                if cer['certification'] == '12세 이상 관람가' or cer['certification'] == '12세 관람가' or cer['certification'] == '12세이상관람가':
                    cer['certification'] = '12'
                if cer['certification'] == '15세 이상 관람가':
                    cer['certification'] = '15'
                if cer['certification'] == '청소년 관람불가' or cer['certification'] == '19':
                    cer['certification'] = '18'                
                c1 = Certification(pk=order_certi[cer['certification']], name=cer['certification'])
                c1.save()
                c1.movies.add(movie)
                break
        else:
            movie.delete()
            continue        

        path3 = path1 + '/watch/providers'
        params3 = {
            'api_key': API_KEY,
            'region' : 'KR',
            'language': 'ko',
        }    
        response3 = requests.get(BASE_URL+path3, params=params3)  
        data3 = response3.json()['results']
        if 'KR' in data3 and 'flatrate' in data3['KR']:
            for d3 in data3['KR']['flatrate']:
                f1 = OTT(pk=d3['provider_id'], name=d3['provider_name'])
                f1.save()
                f1.movies.add(movie)

        path4 = path1 + '/keywords'
        params4 = {
            'api_key': API_KEY,
        }
        response4 = requests.get(BASE_URL+path4, params=params4)
        data4 = response4.json()['keywords']
        for d4 in data4:
            k1 = Keyword(pk=d4['id'], name=d4['name'])
            k1.save()
            k1.movies.add(movie)

        path5 = path1 + '/credits'
        params5 = {
            'api_key': API_KEY,
            'language': 'ko',
        }
        response5 = requests.get(BASE_URL+path5, params=params5)
        data5_cast = response5.json()['cast']
        data5_cast_cut = data5_cast[:5]
        for cast in data5_cast_cut:
            a1 = Actor(pk=cast['id'], name=cast['original_name'])
            a1.profile_path = cast['profile_path'] or ''
            a1.save()
            a1.movies.add(movie)
        data5_crew = response5.json()['crew']
        for crew in data5_crew:
            if crew['job'] == 'Director':
                d1 = Director(pk=crew['id'], name=crew['original_name'])   
                d1.save()
                d1.movies.add(movie)

    return render(request, 'movies/index.html')

def movieid(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    id = str('77117')
    path1 = '/movie/' + id
    params1 = {
        'api_key': API_KEY,
        'language': 'ko',
        'append_to_response': 'releases',
    }
    response1 = requests.get(BASE_URL+path1, params=params1)
    data1 = response1.json()
    movie = Movie()
    movie.pk = id
    movie.title = data1['title']
    movie.orginal_title = data1['original_title']
    if data1['overview'] == '':
        return
    movie.overview = data1['overview']
    movie.poster_path = data1['poster_path']
    if data1['release_date'] == '':
        return
    movie.release_date = data1['release_date']
    movie.runtime = data1['runtime']
    movie.vote_average = data1['vote_average']
    movie.vote_count = data1['vote_count']
    
    path2 = path1 + '/videos'
    params2 = {
        'api_key': API_KEY,
        'language': 'ko',
    }    
    response2 = requests.get(BASE_URL+path2, params=params2)  
    data2 = response2.json()['results']
    
    for d2 in data2:
        movie.video = ''
        if d2['type'] == 'Trailer' or d2['official'] == True:
            movie.video = d2['key']
            break
    if movie.video == '':
        return
    movie.save()

    genres = data1['genres']
    for genre in genres:
        g1 = Genre(pk=genre['id'], name=genre['name'])
        g1.save()
        g1.movies.add(movie)

    certifi = data1['releases']['countries']
    for cer in certifi:
        if cer['iso_3166_1'] == 'KR' and cer['certification'] != '':
            if cer['certification'] == '전체관람가':
                    cer['certification'] = 'ALL'
            if cer['certification'] == '12세 이상 관람가' or cer['certification'] == '12세 관람가' or cer['certification'] == '12세이상관람가':
                cer['certification'] = '12'
            if cer['certification'] == '15세 이상 관람가':
                cer['certification'] = '15'
            if cer['certification'] == '청소년 관람불가' or cer['certification'] == '19':
                cer['certification'] = '18'
            c1 = Certification(pk=order_certi[cer['certification']], name=cer['certification'])
            c1.save()
            c1.movies.add(movie)
            break
    else:
        movie.delete()
        return
    path3 = path1 + '/watch/providers'
    params3 = {
        'api_key': API_KEY,
        'region' : 'KR',
        'language': 'ko',
    }    
    response3 = requests.get(BASE_URL+path3, params=params3)  
    data3 = response3.json()['results']
    if 'KR' in data3 and 'flatrate' in data3['KR']:
        for d3 in data3['KR']['flatrate']:
            f1 = OTT(pk=d3['provider_id'], name=d3['provider_name'])
            f1.save()
            f1.movies.add(movie)

    path4 = path1 + '/keywords'
    params4 = {
        'api_key': API_KEY,
    }
    response4 = requests.get(BASE_URL+path4, params=params4)
    data4 = response4.json()['keywords']
    for d4 in data4:
        k1 = Keyword(pk=d4['id'], name=d4['name'])
        k1.save()
        k1.movies.add(movie)

    path5 = path1 + '/credits'
    params5 = {
        'api_key': API_KEY,
        'language': 'ko',
    }
    response5 = requests.get(BASE_URL+path5, params=params5)
    data5_cast = response5.json()['cast']
    data5_cast_cut = data5_cast[:5]
    for cast in data5_cast_cut:
        a1 = Actor(pk=cast['id'], name=cast['original_name'])
        a1.profile_path = cast['profile_path'] or ''
        a1.save()
        a1.movies.add(movie)
    data5_crew = response5.json()['crew']
    for crew in data5_crew:
        if crew['job'] == 'Director':
            d1 = Director(pk=crew['id'], name=crew['original_name'])   
            d1.save()
            d1.movies.add(movie)

    return render(request, 'movies/id.html')

@api_view(['GET'])
def index(request):
    keyword_list = ['2343', '9840', '180547', '18035', '12565','4344']
    keyword = random.choice(keyword_list)
    movies = Movie.objects.filter(keywords=keyword).order_by('?')[:10]    
    serializer = MovieMainListSerializer(movies,many=True)  
    return Response(serializer.data)
    # random으로 뽑힌 keyword id 값 넣어주는거 고민해보기


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
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