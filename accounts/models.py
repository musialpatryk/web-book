from django.db import models
from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Enter Username...',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Enter Email...',
            })
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Password...'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Re-enter Password...'})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default='None')
    phone = models.CharField(max_length=50, default='None')
    image = models.ImageField(default='profile_images/UserDefault.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username}-Profile'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


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
    )
    address = forms.CharField(
        max_length=50,
    )
    image = forms.ImageField()

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


# Add user to default group during social login
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='viewer'))

