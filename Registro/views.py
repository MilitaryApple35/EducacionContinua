from django.shortcuts import render
from EC.models import Courses
# Create your views here.

def register(request):
    courses = Courses.objects.all()
    return render(request, 'register.html', {'courses':courses})