from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Nazwa użytkownika.',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'E-mail',
            })
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Hasło'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Podaj ponownie hasło'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Login',
            'email': 'Email',
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

    placeholders = {
        'phone': 'None',
        'address': 'None'
    }

    phone = forms.CharField(
        max_length=11,
        label='Telefon'
    )
    address = forms.CharField(
        max_length=50,
        label='Adres'
    )
    image = forms.ImageField(
        label='Obraz'
    )

    def __init__(self, *args, authors=None, genre=None, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-2',
            })

            if field in self.placeholders:
                self.fields[field].widget.attrs.update({
                    'placeholder': self.placeholders[field],
                })
