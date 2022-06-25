from cProfile import label
from pydoc import describe
from sre_parse import CATEGORIES
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass  

class News(models.Model):
    title = models.CharField(max_length=999999999999999999999, unique=True)
    content = models.CharField(max_length=999999999999999999999999999999999999)
    time = models.CharField(max_length=1000)

    def serialize(self):
        return {
            "title": self.title,
            "content": self.content,
            "time": self.time
        }
    

class Event(models.Model):
    title = models.CharField(max_length=999999999999999999999, unique=True)
    describtion = models.CharField(max_length=999999999999999999999)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def serialize(self):
        return {
            "title": self.title,
            "describtion": self.describtion,
            "date": self.date.strftime('%Y-%m-%d')
        }