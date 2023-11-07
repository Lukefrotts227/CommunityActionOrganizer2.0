from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, get_user_model
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    password = forms.charField(label='password')
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password', 'town')
    def clean(self, *args, **kwargs): 
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        town = self.cleaned_data.get('town')
        email_check = get_user_model().objects.filter(email='email')
        if email_check.exists(): 
            raise forms.ValidationError('This Email already exists')
        if len(password) < 5: 
            raise forms.ValidationError('Your password should have more than 5 characters')
        return super(MyUserCreationForm, self).clean(*args, **kwargs)


class MyUserChangeForm(UserChangeForm): 
    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'town')



        