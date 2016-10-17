from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
