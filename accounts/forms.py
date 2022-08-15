from django import forms
from django.forms import ModelForm
from django.core import validators
from accounts.models import User
#import what you will use

class User_form(ModelForm):
    """User form that takes password,username and email"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username","email","password"]
