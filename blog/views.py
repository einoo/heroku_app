# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article

import markdown2


def index(request):
    latest_article_list = Article.objects.query_by_time()
    context = {'latest_article_list': latest_article_list}
    return render(request, 'index.html', context)


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    content = markdown2.markdown(article.content, extras=["code-friendly",
                                                          "fenced-code-blocks",
                                                          "header-ids",
                                                          "toc",
                                                          "metadata"])
    title = article.title
    pub_date = article.pub_date
    return render(request, 'article_page.html', {
        'article': article,
        'content': content,
        'title': title,
        'pub_date': pub_date
    })
