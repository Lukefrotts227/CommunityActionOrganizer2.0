from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model
from .forms import MyUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

User = get_user_model()


def signup_view(request):
    if request.method == 'POST':
        next = request.GET.get('next')
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user= authenticate(email=user.email, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            else:
                return redirect('verify-email')
    else:
        form = MyUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)
    

def verify_email(request): 
    if request.method == 'POST': 
        if request.user.email_is_verified != True:
            current_site = get_current_site
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('registration/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'registration/verify_email.html')

def verify_email_done(request):
    return render(request, 'registration/verify_email_done.html')

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')
        return render(request, 'registration/verify_email_confirm.html')
    
def verify_email_complete(request):
    return render(request, 'registration/verify_email_complete.html')

# Profile update view
@login_required
def profile_update(request):
    # Logic to handle profile update
    pass

def index(request):
     return render(request, 'index.html')


