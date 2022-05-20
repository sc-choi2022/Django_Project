from pprint import pprint
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
        'page': 17,
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()['results']
    for d in data:
        movie = Movie()
        movie.title = d['title']
        movie.orginal_title = d['original_title']
        if d['overview'] == '':
            break
        movie.overview = d['overview']
        movie.poster_path = d['poster_path']
        movie.vote_average = d['vote_average']
        movie.vote_count = d['vote_count']
        # genres = d['genre_ids']
        # for genre in genres:
        #     mm = {28: '액션'}
        #     g1 = Genre(pk=genre, name=mm[genre])
        #     g1.save()
        #     movie.genres.add(g1)
        # movie.genres = d['genre_ids']
        movie.release_date = d['release_date']
        if d['release_date'] == '':
            continue
        id = d['id']
        path1 = '/movie/' + str(id)
        params1 = {
            'api_key': API_KEY,
            'language': 'ko',
            'append_to_response': 'releases',
        }
        response1 = requests.get(BASE_URL+path1, params=params1)
        data1 = response1.json()
        movie.runtime = data1['runtime']
        certifi = data1['releases']['countries']
        for cer in certifi:
            if cer['iso_3166_1'] == 'KR':
                movie.certification_set = cer['certification']
                break
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
        path3 = path1 + '/credits'
        params3 = {
            'api_key': API_KEY,
            'language': 'ko',
        }
        response3 = requests.get(BASE_URL+path3, params=params3)
        data3_cast = response3.json()['cast']
        data3_cast_cut = data3_cast[:5]
        cast_list = []
        for cast in data3_cast_cut:
            cast_list.append(cast['original_name'])
        movie.actors_set = cast_list
        data3_crew = response3.json()['crew']
        for crew in data3_crew:
            if crew['job'] == 'Director':
                movie.directors_set = crew['original_name']
        movie.save()
    return render(request, 'movies/index.html')