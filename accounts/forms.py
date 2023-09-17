

from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(forms.ModelForm):
    """For user registration"""
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'primary_phone', 'first_name', 'last_name']

        