from EC.models import Courses, Capacitaciones, Diplomados, Congresos, Conferencias, Talleres
from django.shortcuts import render
# Importa el modelo Box (representa los datos de las cajas)

def main(request):
    '''
    Args: None
    Process:None
    Return:Devuelve el render de la pagina principal.
    '''
    courses = Courses.objects.all()
    capacitaciones= Capacitaciones.objects.all()
    diplomados = Diplomados.objects.all()
    congresos = Congresos.objects.all()
    conferencias = Conferencias.objects.all()
    talleres = Talleres.objects.all()
    return render(request,'index.html',  {'courses': courses , 'capacitaciones': capacitaciones,'diplomados': diplomados, 'congresos': congresos, 'conferencias': conferencias, 'talleres': talleres})


    