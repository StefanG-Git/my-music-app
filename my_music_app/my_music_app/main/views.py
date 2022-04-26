from django.http import HttpResponse
from django.shortcuts import render


def show_home(request):
    return HttpResponse('<h1>It works!<h1/>')


def add_album(request):
    pass


def album_details(request, pk):
    pass
