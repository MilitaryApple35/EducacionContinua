from django.shortcuts import render
from EC.models import Courses
from .forms import RegistroForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = RegistroForm()
    courses = Courses.objects.all()
    return render(request, 'register.html', {'courses':courses}, {'form':form})