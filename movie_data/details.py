import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def details():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/496243'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'en-US',
        'append_to_response': 'releases',
        'video': True,
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    pprint(data)

details()