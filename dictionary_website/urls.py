from django.urls import path

from .views import home

app_name = 'dict_website'

urlpatterns = [
    path('',home)
]