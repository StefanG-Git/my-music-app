from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.main.validators import validate_only_letters_and_underscore


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_only_letters_and_underscore
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MUSIC_GENRES = (
        'Pop Music',
        'Jazz Music',
        'R & B Music',
        'Rock Music',
        'Country Music',
        'Dance Music',
        'Hip Hop Music',
        'Other',
    )

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=[(g, g) for g in MUSIC_GENRES],
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )
