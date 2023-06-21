from EC.models import Courses
from django.shortcuts import render
# Importa el modelo Box (representa los datos de las cajas)

def main(request):
    '''
    Args: None
    Process:None
    Return:Devuelve el render de la pagina principal.
    '''
    courses = Courses.objects.all()
    return render(request,'index.html',  {'courses': courses})


    