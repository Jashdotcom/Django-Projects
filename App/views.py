from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .forms import login,logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.gget_user()
            login(request, user)

    else:
        form =  AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/login')

    return redirect('/login')



