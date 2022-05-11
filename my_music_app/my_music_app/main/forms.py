from django import forms

from my_music_app.main.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                },
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                },
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'name',
            'artist',
            'genre',
            'description',
            'image_url',
            'price',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                },
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                },
            ),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            'name',
            'artist',
            'genre',
            'description',
            'image_url',
            'price',
        )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                },
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                },
            ),
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = (
            'name',
            'artist',
            'genre',
            'description',
            'image_url',
            'price',
        )
