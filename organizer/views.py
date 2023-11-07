from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm
from .utils import send_verification_email
from django.utils.decorators import method_decorator
from .decorators import email_verified_required


# Registration view
class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form): 
        user = form.save(commit=False)
        user.is_active = False
        send_verification_email(user, self.request)
        return super().form_valid(form)

# Profile update view
@method_decorator(email_verified_required, name='dispatch')
def profile_update(request):
    # Logic to handle profile update
    pass

def index(request):
     return render(request, 'index.html')


