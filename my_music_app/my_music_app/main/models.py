from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15
    USERNAME_PATTERN = r'^\w+$'
    INVALID_USERNAME_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            RegexValidator(USERNAME_PATTERN, INVALID_USERNAME_MESSAGE),
        ),
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_TYPE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0

    MUSIC_GENRES = (
        'Pop Music',
        'Jazz Music',
        'R&B Music',
        'Rock Music',
        'Country Music',
        'Dance Music',
        'Hip Hop Music',
        'Other',
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_TYPE_MAX_LENGTH,
        choices=[(g, g) for g in MUSIC_GENRES],
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
