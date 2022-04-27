from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
        ]
    )

    email = models.EmailField(
        null=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ]
    )
