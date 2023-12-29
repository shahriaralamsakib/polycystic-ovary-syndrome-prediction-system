from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField()
        password = forms.CharField()

class PCOSForm(forms.ModelForm):
    class Meta:
        model = PolycysticOvarySyndromeModel
        fields = '__all__'
