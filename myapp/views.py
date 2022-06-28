import email
from django.shortcuts import render
from urllib3 import HTTPResponse

# Create your views here.
def index(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    return render(request, 'index.html')
    