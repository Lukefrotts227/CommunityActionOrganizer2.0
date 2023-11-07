from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def email_verified_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if not authenticated
        if not request.user.email_verified:
            return HttpResponseForbidden("Please verify your email to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

