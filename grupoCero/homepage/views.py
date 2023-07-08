from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'gallery.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def loginPage(request):
    return render(request, 'login-page.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('home_page')
    else:
        messages.success(request, 'Ha habido un error. Prueba de nuevo.')
        return redirect('login_page')

def register_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        messages.success(request, 'Usuario registrado con exito')
        return redirect('login_page')
    else:
        messages.success(request, 'No se ha podido crear el usuario.')
        return redirect('login_page')
def logout_user(request):
    logout(request)
    messages.success(request, "Sesion cerrada con éxito." )
    return redirect('login_page')
