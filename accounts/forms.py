from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, 
                                        PasswordChangeForm, PasswordResetForm)
from .models import CustomUser



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label = 'Email')
    error_messages = {
        'invalid_login': (
            "Please enter a correct Email and Password. Note that both "
            "fields may be case-sensitive."
        ),
    }

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1','password2']
