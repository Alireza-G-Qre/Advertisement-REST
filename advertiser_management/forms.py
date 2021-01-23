from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators
from .models import *

User = get_user_model()


class AdvertiserCreationForm(UserCreationForm):
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
    #     label='Username',
    #     validators=[
    #         validators.MaxLengthValidator(limit_value=30, message='Number of character must be lower than 30.'),
    #         validators.MinLengthValidator(8, 'Number of character must be at least 8.')
    #     ]
    # )
    #
    # email = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}),
    #     label='Email',
    #     validators=[
    #         validators.EmailValidator('Invalid email entered'),
    #         validators.MaxLengthValidator(200, 'Number of character must be lower than 200.')
    #     ]
    # )
    #
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
    #     label='Password',
    #     validators=[
    #         validators.RegexValidator(
    #             regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
    #             message='Minimum eight characters, at least one letter and one number',
    #         )
    #     ]
    # )
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     is_exists_user_by_email = User.objects.filter(email=email).exists()
    #
    #     if is_exists_user_by_email:
    #         raise forms.ValidationError('Duplicate email.')
    #
    #     return email
    #
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     is_exists_user_by_username = User.objects.filter(username=username).exists()
    #
    #     if is_exists_user_by_username:
    #         raise forms.ValidationError('Duplicate username')
    #
    #     return username

    class Meta(UserCreationForm):
        model = Advertiser
        fields = ('username', 'password', 'email')


class AdvertiserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Advertiser
        fields = ('username', 'password', 'email', 'clicks', 'views')


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


class AdvertiseRegister(UserCreationForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Title'}),
        label='Title',
        validators=[
            validators.MaxLengthValidator(limit_value=30, message='Number of character must be lower than 30.'),
            validators.MinLengthValidator(8, 'Number of character must be at least 8.')
        ]
    )

    img_url = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your URL'}),
        label='URL',
        validators=[
            validators.URLValidator(),
            validators.RegexValidator(
                regex=r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)',
                message='Please enter a valid URL.'
            )
        ]
    )

    link = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Link'}),
        label='Link',
        validators=[
            validators.URLValidator(),
            validators.RegexValidator(
                regex=r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)',
                message='Please enter a valid URL.'
            )
        ]
    )

    class Meta(UserCreationForm):
        model = Advertiser
        fields = ('title', 'img_url', 'link')
