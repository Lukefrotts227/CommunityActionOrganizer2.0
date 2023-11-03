from django.urls import path

from .views import index, api_test, route_test

urlpatterns = [
    path('', index, name='index'),
]