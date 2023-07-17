from django.shortcuts import render 
from django.http import HttpResponseRedirect
from EC.models import Courses

def Login(request):
    return render(request,'login.html');
