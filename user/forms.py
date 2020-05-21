from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import SecurityCode

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class SecurityCodeForm(forms.ModelForm):
    class Meta:
        model = SecurityCode
        fields = ['code']