from multiprocessing import AuthenticationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from HomeApp import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

#Password for User1 is : User1_1111

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def logout(request):
    auth_logout(request)
    return redirect('/')