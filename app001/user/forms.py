from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2' ]
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 300px', 'type': 'text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))