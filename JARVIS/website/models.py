from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_date = models.DateTimeField('date answered')
