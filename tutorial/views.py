from urllib import request
from django.http import HttpResponse, response
from django.shortcuts import render

def first_page(request):
    a = 'Hi there!'
    text = 'Some text...'
    return render(request, './index.html', {
        'a': a,
        'text': text
    })