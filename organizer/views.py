# organizer/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.htmx:
        # This is an htmx request, return a partial
        return HttpResponse('<p>This is an htmx response!</p>')
    else:
        # This is a full page request
        return render(request, 'index.html')

def api_test(request): # This is
    return HttpResponse('<p>This is an htmx response!</p>')
