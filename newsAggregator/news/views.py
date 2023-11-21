from django.shortcuts import render
import requests

from django.conf import settings


API_KEY = settings.NEWS_API_KEY

COUNTRY = settings.COUNTRY_CODE


def news_lists(request):

    if request.method == 'GET':
        url = f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={API_KEY}'
        res = requests.get(url).json()
        news_articles = res['articles']
        context = {
            'news_articles': news_articles
        }
        return render(request, 'news/home.html', context)

    return render(request, 'news/home.html')
