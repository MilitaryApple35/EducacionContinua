# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from EC.models import Courses
from .forms import CoursesForm
from django.http import HttpResponse, HttpResponseRedirect


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

def editar_curso(request, curso_id):
    curso = get_object_or_404(Courses, pk=curso_id)

    if request.method == 'POST':
        imagen = request.POST['imagen']
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']

        curso.imagen = imagen
        curso.titulo = titulo
        curso.descripcion = descripcion
        curso.save()

        # Redirige al usuario a la página de administración con un mensaje de éxito
        return redirect('administracion')

    return render(request, 'editar_curso.html', {'curso': curso})

def eliminar_curso (request, curso_id):
    curso = get_object_or_404(Courses,pk=curso_id)

    if request.method == 'POST':
        curso.delete()
        return redirect(administracion)
    return render(request,'eliminar_curso.html',{'curso':curso})


@login_required
def administracion(request):
    # Tu código de la vista de administración aquí
    cursos = Courses.objects.all()
    return render(request, 'administracion.html', {'cursos': cursos})

