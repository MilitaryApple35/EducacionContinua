from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from EC.models import Courses
from .forms import RegistroForm
from EC.views import main
# Create your views here.

def register(request):
    courses = Courses.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RegistroForm()
    
    return render(request, 'register.html', {'courses': courses, 'form': form, 'errors': form.errors})

