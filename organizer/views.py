# organizer/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import baseUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Registration view
class SignUpView(generic.CreateView):
    form_class = baseUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Profile update view
@login_required
def profile_update(request):
    # Logic to handle profile update
    pass


# Create your views here.
def index(request):
     return render(request, 'index.html')


