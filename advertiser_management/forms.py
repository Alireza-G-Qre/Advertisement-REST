from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AdvertiserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class LoginAdvertiserForm(Form):
    class Meta(Form):
        model = Advertiser
        fields = ('username', 'password')


class AdvertiseCreationForm(ModelForm):
    class Meta(UserCreationForm):
        model = Ad
        fields = ('title', 'image_url', 'link', 'description')
