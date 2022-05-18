import requests
from pprint import pprint


def certification():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/certification/movie/list'
    params = {
        'api_key': 'fe2db36141a69429c6342aba799b9367',
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    pprint(data)

certification()