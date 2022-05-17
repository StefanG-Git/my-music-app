from django.shortcuts import render, redirect

from my_music_app.main.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
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
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = AddAlbumForm()

    context = {
        'form': form
    }

    return render(request, 'albums/add-album.html', context)


def show_album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def show_profile_details(request):
    profile = get_profile()
    albums_count = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile/profile-delete.html', context)
