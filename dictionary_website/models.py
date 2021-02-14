from django.db import models
from django.db.models.signals import post_save
from datetime import timedelta

class WordOfTheDay(models.Model):
    word=models.CharField(max_length=225)
    definition=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)


def timeChange_post_save(sender,instance,created,*args,**kwargs):
   
    if created:
        print(instance.timestamp)
        deadline=instance.timestamp+timedelta(hours=23)
        instance.word='ghana'
        instance.timestamp=deadline
        instance.save()
        print(instance.timestamp)

post_save.connect(timeChange_post_save,sender=WordOfTheDay)