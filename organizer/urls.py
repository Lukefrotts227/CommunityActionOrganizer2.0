from django.urls import path

from .views import index, api_test

urlpatterns = [
    path('', index, name='index'),
    path('api/test', api_test, name='api_test')
]