import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def watch_providers():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/524434/watch/providers'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()['results']

    pprint(data)

watch_providers()