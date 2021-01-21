from django.shortcuts import render

def home(request):
    return render(request,'dictionary_website/home.html')
