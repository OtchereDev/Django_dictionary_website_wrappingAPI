import requests
import os

def contactAPI(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        'x-rapidapi-key': os.getenv('API_KEYS'),
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()

