#!/usr/bin/env python3

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default error messages to be empty or customize them
        self.fields['password1'].error_messages = {
            'password_too_similar': '',
            'password_too_short': '',
            'password_entirely_numeric': '',
            'password_common': '',
        }
        self.fields['password2'].error_messages = {
            'password_too_similar': '',
            'password_too_short': '',
            'password_entirely_numeric': '',
            'password_common': '',
        }
