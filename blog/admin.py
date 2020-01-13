# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Author, Article


class ArticleInline(admin.StackedInline):
    model = Article
    readonly_fields = ['pub_date']
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Email', {'fields': ['email'], 'classes':['collapse']}),
    ]
    list_display = ('name', 'email')
    inlines = [ArticleInline]


admin.site.register(Author, AuthorAdmin)
