from django.urls import path
from django.urls import path
from .views import SignUpView, profile_update
from django.contrib.auth import views as auth_views

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/update/', profile_update, name='profile_update'),

]