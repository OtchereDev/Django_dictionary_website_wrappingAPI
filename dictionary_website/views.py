from django.shortcuts import render
from .helpers import contactAPI

def home(request):

    context={}

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
