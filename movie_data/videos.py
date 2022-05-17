import requests
from pprint import pprint


def videos():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/278/videos'
    params = {
        'api_key': 'fe2db36141a69429c6342aba799b9367',
        'region': 'KR',
        'language': 'en-US',
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    pprint(data)

videos()