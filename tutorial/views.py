from urllib import request
from django.http import HttpResponse, response
from django.shortcuts import render

def first_page(request):
    a = '<h1>Hi there!</h1>'
    text = '<p>Some text...</p>'
    return render(request, '/index.html', {
        'a': a,
        'text': text
    })