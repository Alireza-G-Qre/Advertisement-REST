from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.core import validators
from .models import *

User = get_user_model()


class AdvertiserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Advertiser
        fields = ('username', 'password1', 'password2', 'email')


class AdvertiserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Advertiser
        fields = ('username', 'password', 'email', 'clicks', 'views')


class AdvertiseCreationForm(ModelForm):
    class Meta(UserCreationForm):
        model = Advertise
        fields = ('title', 'image_url', 'link', 'description')


class LoginAdvertiser(forms):
    pass

    def clean_username(self):
        username = self.cleaned_data['username']
        is_user = User.objects.filter(username=username).exists()

        if not is_user:
            raise forms.ValidationError('Username not found.')

        return username
