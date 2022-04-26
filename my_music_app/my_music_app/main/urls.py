from django.urls import path
from my_music_app.main.views import show_home, add_album, album_details

urlpatterns = (
    path('', show_home),
    path('album/add/', add_album),
    path('album/details/<int:id>/', album_details)
)
