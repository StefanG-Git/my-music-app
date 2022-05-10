from django.urls import path
from my_music_app.main.views import show_home, add_album, show_album_details, edit_album, delete_album, \
    show_profile_details, delete_profile

urlpatterns = (
    path('', show_home, name='show home'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:id>/', show_album_details, name='show album details'),
    path('album/edit/<int:id>/', edit_album, name='edit album'),
    path('album/delete/int:<id>/', delete_album, name='delete album'),
    path('profile/details/', show_profile_details, name='show profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
