from django.shortcuts import render, redirect

from my_music_app.main.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'albums': Album.objects.all(),
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    return render(request, 'add-album.html')


def show_album_details(request, pk):
    pass


def edit_album(request, pk):
    pass


def delete_album(request, pk):
    pass


def show_profile_details(request):
    albums_count = len(Album.objects.all())
    context = {
        'profile': get_profile(),
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    return render(request, 'profile-delete.html')


def create_profile(request):
    return render(request, 'home-no-profile.html')
