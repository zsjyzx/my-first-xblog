from django.db import models
from mdeditor.fields import MDTextField
#from mdeditor.fields import MDTextFormField

class Article(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=50)
    title_zh = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content_md = MDTextField()
    content_html = models.TextField()
    # type = models.CharField(max_length=30)  #django, python, ...
    tags = models.CharField(max_length=30)
    views = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()
