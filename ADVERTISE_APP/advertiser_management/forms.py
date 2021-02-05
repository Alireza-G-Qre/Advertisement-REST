from django.forms import ModelForm, BooleanField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AdvertiserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class LoginAdvertiserForm(AuthenticationForm):
    remember_me = BooleanField(required=False)

    class Meta(AuthenticationForm):
        model = Advertiser
        fields = ('username', 'password', 'remember_me')


class AdvertiseCreationForm(ModelForm):
    class Meta(UserCreationForm):
        model = Ad
        fields = ('title', 'img_Url', 'linkUrl', 'description')
