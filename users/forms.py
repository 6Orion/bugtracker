from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import ClearableFileInput

from .models import CustomUser



class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/customclearablefileinput.html'


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'image',)

        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
            'image': 'Avatar imagee',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your e-mail address'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your surname'}),
            'image': CustomClearableFileInput(attrs={'class':'form-control', 'placeholder':'Your avatar image'}),
        }
