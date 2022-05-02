from django.urls import path
from my_music_app.main.views import show_home, add_album, show_album_details, edit_album, delete_album, \
    show_profile_details, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:id>/', show_album_details, name='album details'),
    path('album/edit/<id>/', edit_album, name='edit album'),
    path('album/delete/<id>/', delete_album, name='delete album'),
    path('profile/details/', show_profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
