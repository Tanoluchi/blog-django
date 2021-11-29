from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html', {
        'title': 'Inicio',
    })

def about(request):
    return render(request, 'main_app/about.html', {
        'title': 'Sobre nosotros',
    })

def register_page(request):
    # Si el usuario ya se encuentra identificado, lo redirrecionamos a inicio
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # Formulario de registro
        register_form = RegisterForm()

        # Guardar usuario para cuando envien sus datos.
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            # En caso de que el formulario es valido, lo guardamos
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente!')

                return redirect('home')

        return render(request, 'user/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    # Si el usuario ya se encuentra identificado, lo redirrecionamos a inicio
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # Si nos llega informacion del formulario
        if request.method == 'POST':
            # Vamos a crear unas variables que van a guardar dentro la informacion necesaria
            # para poder iniciar sesion
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Le pasamos la informacion recogida (nombre de usuario y contraseña)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'No te has identificado correctamente!')


        return render(request, 'user/login.html', {
            'title': 'Identificarse',
        })

def logout_user(request):
    logout(request)

    return redirect('login')