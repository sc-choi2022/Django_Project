import requests
from pprint import pprint


def details():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243'
    params = {
        'api_key': 'fe2db36141a69429c6342aba799b9367',
        'region': 'KR',
        'language': 'en-US',
        'append_to_response': 'releases',
        'video': True,
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    pprint(data)

details()