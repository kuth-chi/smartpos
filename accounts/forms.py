

from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .utils import is_phone_number


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

    def clean(self):
        cleaned_data = super().clean()
        input_value = cleaned_data.get('email')

        if not is_phone_number(input_value):
            try:
                validate_email(input_value)
                cleaned_data['email'] = input_value
            except ValidationError as exc:
                raise ValidationError(_('Invalid email address or phone number')) from exc
        return cleaned_data
        