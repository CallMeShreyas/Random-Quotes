from django.shortcuts import render
import requests
import random
# Create your views here.


def index(request):
    responce = requests.get("https://type.fit/api/quotes")
    res = responce.json()
    rand_quote = random.randint(0, 1643)
    quote = res[rand_quote]
    text = quote['text']
    author = quote['author']

    return render(request, 'index.html', {'quote': text, 'author': author})
