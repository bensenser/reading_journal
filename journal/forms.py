from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ReadBook

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class ReadBookForm(forms.ModelForm):
    class Meta:
        model = ReadBook
        fields = ['title', 'author', 'start_date', 'end_date', 'main_characters', 'description', 'rating']
