from django.core.validators import MinLengthValidator
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
