from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter username'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter last name'}),
            'email': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter email'}),
            'password': forms.PasswordInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter password'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter email'}),
            'password': forms.PasswordInput(attrs={'class': 'w-full p-3 border rounded', 'placeholder': 'Enter password'}),
        }