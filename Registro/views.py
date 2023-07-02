from django.shortcuts import render 

from EC.models import Courses
from .forms import RegistroForm
# Create your views here.

def register(request):
    courses = Courses.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'courses': courses, 'form': form},)
 