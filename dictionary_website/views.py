from django.shortcuts import render
from .helpers import contactAPI,word_of_the_day

def home(request):

    
    random_word=word_of_the_day()

    context={
        'method':'GET',
        'word':random_word['word'],
        'definition':random_word['definition']
    }

    if request.method =='POST':
        search_word = request.POST.get('search_word')
       
        search_result=contactAPI(search_word)
        try:
        
            context={
                'word':search_result['word'],
                'pronunciation':search_result['pronunciation'],
                'results':search_result['results'],
                'method':'POST'
            }
        except KeyError:
            if search_result['success'] == False:
                context={
                    'error':search_result['message']
                }

    return render(request,'dictionary_website/home.html',context=context)
