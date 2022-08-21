from secrets import choice
from django.utils import timezone
from django.db import models
import datetime as dt
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('Date Publised')
    
    def was_published_recently(self):
        now =timezone.now()
        return now - dt.datetime.timedelta(days =1) <= self.publication_date <= now
        # return self.publication_date >= timezone.now() - dt.timedelta(days = 1)
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text