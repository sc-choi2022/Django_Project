import requests
from django.shortcuts import render
from movies.models import Movie, Genre, Actor
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def movie(request):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
        'page': 1,
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
    return render(request, 'movies/index.html')