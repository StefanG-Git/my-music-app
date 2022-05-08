from django.http import HttpResponse
from django.shortcuts import render


def show_home(request):
    return render(request, 'home-no-profile.html')


def add_album(request):
    pass


def show_album_details(request, pk):
    pass


def edit_album(request, pk):
    pass


def delete_album(request, pk):
    pass


def show_profile_details(request):
    pass


def delete_profile(request):
    pass
