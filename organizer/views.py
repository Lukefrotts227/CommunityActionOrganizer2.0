from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm




# Registration view
class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

# Profile update view
@login_required
def profile_update(request):
    # Logic to handle profile update
    pass

def index(request):
     return render(request, 'index.html')


