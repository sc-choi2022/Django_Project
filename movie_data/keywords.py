import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def keywords():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243/keywords'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    pprint(data)

keywords()