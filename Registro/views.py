from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from EC.models import Courses, Capacitaciones, Diplomados, Conferencias, Congresos, Talleres
from .forms import RegistroForm
from EC.views import main
# Create your views here.

def register(request):
    courses = Courses.objects.all()
    capacitaciones= Capacitaciones.objects.all()
    diplomados = Diplomados.objects.all()
    congresos = Congresos.objects.all()
    conferencias = Conferencias.objects.all()
    talleres = Talleres.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RegistroForm()
    
    return render(request, 'register.html', {'courses': courses, 'form': form, 'errors': form.errors , 'capacitaciones': capacitaciones,'diplomados': diplomados, 'congresos': congresos, 'conferencias': conferencias, 'talleres': talleres})
