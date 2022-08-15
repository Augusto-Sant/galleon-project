from django import forms
from django.forms import ModelForm
from django.core import validators
from accounts.models import User
#LEMBRE-SE DE IMPORTAR TUDO QUE FOR USAR

class User_form(ModelForm):#MODEL FORM É DIFERENTE DE UM FORM PORQUE VAI DIRETO PRO MODEL (SUAS CARACTERISTICAS)
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username","email","password"]
