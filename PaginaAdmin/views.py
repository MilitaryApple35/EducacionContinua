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
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from EC.models import Courses
from .forms import CoursesForm
from django.views.generic.edit import FormView


# ARREGLAR ESTO

def agregarCurso(request):
    courses = Courses.objects.all()
    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('loginadministracion/')
    else:
        form = CoursesForm()

    return render(request, 'administracion.html', {'courses': courses, 'form': form, 'errors': form.errors})

def login_view(request):
    return render(request,'login.html')

@login_required
def administracion(request):
    # Tu código de la vista de administración aquí
    cursos = Courses.objects.all()
    return render(request, 'administracion.html', {'cursos': cursos})

