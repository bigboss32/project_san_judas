from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido, {username}. Has iniciado sesión con éxito.")
                return redirect('index')  # Reemplaza 'inicio' con la URL a la que quieres redirigir después del inicio de sesión.
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'incio_sesion.html', {'form': form})

def registrar_usuario(request):
  if request.method == 'POST':
        try:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            if password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )

                login(request, user)
                return redirect('iniciar_sesion') 
            else:
                return render(request, 'registro_usuario.html', {'error': 'Las contraseñas no coinciden'})
        except Exception as e:
            return render(request, 'registro_usuario.html', {'error': str(e)})
  return render(request, 'registro_usuario.html')
