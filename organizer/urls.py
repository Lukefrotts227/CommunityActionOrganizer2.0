from django.urls import path
from .views import SignUpView, profile_update
from django.contrib.auth import views as auth_views

from .views import index, signup_view, verify_email, verify_email_done, verify_email_confirm, verify_email_complete

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('verify-email/', verify_email, name='verify-email'),
    path('verify-email/done/', verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', verify_email_complete, name='verify-email-complete'),
    path('signup/', signup_view, name='signup'),
    path('profile/update/', profile_update, name='profile_update'),

]