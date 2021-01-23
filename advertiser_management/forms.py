from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class AdvertiseRegister(UserCreationForm):
    class Meta(UserCreationForm):
        model = Advertise
        fields = ('title', 'image_url', 'link', 'description')


class LoginAdvertiser(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
        label='Username',
        validators=[
            validators.MaxLengthValidator(limit_value=30, message='Number of character must be lower than 30.'),
            validators.MinLengthValidator(8, 'Number of character must be at least 8.')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
        label='Password',
        validators=[
            validators.RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message='Minimum eight characters, at least one letter and one number',
            )
        ]
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        is_user = User.objects.filter(username=username).exists()

        if not is_user:
            raise forms.ValidationError('Username not found.')

        return username
