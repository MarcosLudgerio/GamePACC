from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile', 'password1', 'password2']