from django.utils import timezone

import requests
import os
from datetime import timedelta

from .models import WordOfTheDay

def contactAPI(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        'x-rapidapi-key': os.getenv('API_KEYS'),
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()


def get_random_word():
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random":"true"}

    headers = {
        'x-rapidapi-key': os.getenv('API_KEYS'),
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()



def word_of_the_day():
    current_word=WordOfTheDay.objects.last()
    if current_word:
        word_add_time = current_word.timestamp+timedelta(hours=23)
        
        if word_add_time > timezone.now():
            words_day ={'word':current_word.word,
                        'definition':current_word.definition}
            return words_day

        else:
            
            current_word.delete()
            
            data=get_random_word()
            
            random_word=data['word']
            definition=data['results'][0]['definition']
            WordOfTheDay.objects.create(word=random_word,definition=definition)

            words_day ={'word':random_word,
                        'definition':definition}
            return words_day

    else:
            
        data=get_random_word()
        
        random_word=data['word']
        definition=data['results'][0]['definition']
        WordOfTheDay.objects.create(word=random_word,definition=definition)

        words_day ={'word':random_word,
                    'definition':definition}
        return words_day

