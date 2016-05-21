from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=256)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null = True)
	likes = models.ManyToManyField(User, related_name = 'qlikes')
        class Meta:
                db_table = 'question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question, null = True)
	author = models.ForeignKey(User, null = True)
        class Meta:
                db_table = 'answer'

