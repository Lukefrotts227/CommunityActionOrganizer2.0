# organizer/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
     return render(request, 'index.html')


