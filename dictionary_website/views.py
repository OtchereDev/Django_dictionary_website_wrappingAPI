from django.shortcuts import render
from .helpers import contactAPI

def home(request):

    if request.method =='POST':
        search_word = request.POST.get('search_word')
        for i in contactAPI(search_word)['results']:
            print(i)
            print()
            print()
    return render(request,'dictionary_website/home.html')
