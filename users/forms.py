from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserLoginForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username input input-bordered input-primary w-full max-w-xs'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'email input input-bordered input-primary w-full max-w-xs'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password input input-bordered input-primary w-full max-w-xs'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password input input-bordered input-primary w-full max-w-xs'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username input input-bordered input-primary w-full max-w-xs'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password input input-bordered input-primary w-full max-w-xs'}))

    class Meta:
        model = User
        fields = ['username', 'password']
