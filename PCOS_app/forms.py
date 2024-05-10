from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField()
        password = forms.CharField()

class PCOSForm(forms.ModelForm):
    class Meta:
        model = PolycysticOvarySyndromeModel
        fields = ['folicle_no_R', 'folicle_no_L', 'cycle_r_i', 'cycle_len_days', 'amh_ng_ml', 'fsh_lh', 'prl_ng_ml', 'waist_hip_ratio', 'skin_d_Y', 'skin_d_N', 'hair_g_Y', 'hair_g_N', 'fastFood_Y', 'fastFood_N', 'weight_Y', 'weight_N']
