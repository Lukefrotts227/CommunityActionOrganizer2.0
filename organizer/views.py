# organizer/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # This is a full page request
    return render(request, 'index.html')


