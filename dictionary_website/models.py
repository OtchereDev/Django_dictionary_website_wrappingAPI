from django.db import models


class WordOfTheDay(models.Model):
    word=models.CharField(max_length=225)
    definition=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)

