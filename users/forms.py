from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('password', 'first_name', 'last_name', 'email', 'image')

        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
            'image': 'Avatar image',
            'password': 'Password',
            
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your e-mail address'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your surname'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':'Your avatar image'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your password'}),
        }