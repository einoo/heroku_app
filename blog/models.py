# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=70, null=True,
                              blank=True, unique=True)

    def __unicode__(self):
        return self.name


class ArticleManager(models.Manager):

    def query_by_time(self):
        query = self.get_queryset().order_by('-pub_date')
        return query


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField('content')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __unicode__(self):
        return self.title

    objects = ArticleManager()
