from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')

def registro_usuario(request):

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()


        if not username or not password:
            messages.error(request, "Todos los  campos son obligatorios")
            return redirect('registro')

        try:
            User.objects.create_user(
                username=username,
                password=password
            )

            messages.success(request, "Usuario registrado exitosamente")
            return redirect('login')


        except IntegrityError:
            messages.error(request,"El Usuario ya existe")
            return redirect('registro')

    return render(request, 'usuarios/registro.html')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)

        if user is  not None:
            login(request, user)
            messages.success(request, "Bienvenido 👋")

            return redirect('index')
        
        messages.error(request, "Usuario o contraseña incorrectos")
        return redirect('login')

    return render(request,'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('index')


