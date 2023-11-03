from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import baseUser
class baseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = baseUser
        