from django.shortcuts import render

from my_music_app.main.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return render(request, 'home-no-profile.html')

    context = {
        'profile': profile,
        'albums': Album.objects.all(),
    }

    return render(request, 'home-with-profile.html', context)


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
