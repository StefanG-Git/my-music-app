from django.urls import path
from my_music_app.main.views import home

urlpatterns = (
    path('', home),
)
