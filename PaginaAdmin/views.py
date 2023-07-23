# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from EC.models import Courses

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administracion')
        else:
            # Si el usuario no existe o las credenciales son incorrectas, puedes mostrar un mensaje de error en la plantilla
            error_message = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def administracion(request):
    # Tu código de la vista de administración aquí
    cursos = Courses.objects.all()
    return render(request, 'administracion.html', {'cursos': cursos})
