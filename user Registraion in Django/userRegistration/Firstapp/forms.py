from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#add extra field email using user registration form
class UserRegistrationForm(UserCreationForm):
    Email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','password1','password2']
