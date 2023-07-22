# views.py
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def administracion(request):
    # Tu código de la vista de administración aquí
    cursos = Curso.objects.all()
    return render(request, 'administracion.html', {'cursos': cursos})
