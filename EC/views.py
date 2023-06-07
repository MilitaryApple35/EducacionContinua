from django.shortcuts import render
# Importa el modelo Box (representa los datos de las cajas)

def main(request):
    '''
    Args: None
    Process:None
    Return:Devuelve el render de la pagina principal.
    '''
    return render(request,'index.html')
def cursos(request):
    courses = Course.objects.all()
    return render(request, 'cursos.html', {'courses': courses})

    