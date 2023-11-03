from django.urls import path

from .views import index, api_test, route_test

urlpatterns = [
    path('', index, name='index'),
    path('api/test', api_test, name='api_test'),
    path('route/test', route_test, name='route_test')
]