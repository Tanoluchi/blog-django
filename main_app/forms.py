from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegisterForm(UserCreationForm):
    class Meta:
        # El modelo en el que se va a basar es el de User
        model = User
        # Los campos que queremos que se muestren para rellenar
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

