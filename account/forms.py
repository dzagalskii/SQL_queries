from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
