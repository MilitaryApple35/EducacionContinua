# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from EC.models import Courses, Registro
from .forms import CoursesForm
from django.http import HttpResponse, HttpResponseRedirect
<<<<<<< Updated upstream
from django.views.generic.edit import FormView
from django.urls import reverse
=======
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

>>>>>>> Stashed changes

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administracion')
        else:
            # Si el usuario no existe o las credenciales son incorrectas, puedes mostrar un mensaje de error en la plantilla
            error_message = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def agregarCurso(request):
    courses = Courses.objects.all()
    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracion'))
    else:
        form = CoursesForm()

    return render(request, 'administracion.html', {'courses': courses, 'form': form, 'errors': form.errors})

def editar_curso(request, curso_id):
    curso = get_object_or_404(Courses, pk=curso_id)

    if request.method == 'POST':
        imagen = request.POST['imagen']
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']

        curso.imagen = imagen
        curso.titulo = titulo
        curso.descripcion = descripcion
        curso.save()

        # Redirige al usuario a la página de administración con un mensaje de éxito
        return redirect('administracion')

    return render(request, 'editar_curso.html', {'curso': curso})

def eliminar_curso (request, curso_id):
    curso = get_object_or_404(Courses,pk=curso_id)

    if request.method == 'POST':
        curso.delete()
        return redirect(administracion)
    return render(request,'eliminar_curso.html',{'curso':curso})


@login_required
def administracion(request):
    # Tu código de la vista de administración aquí
    cursos = Courses.objects.all()
    return render(request, 'administracion.html', {'cursos': cursos})


class ReporteExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        query = Registro.objects.all()
        wb = Workbook()
        cont = 1
        ws = wb.active
        ws.title = "Hoja"+str(cont)
        AlinTitulo = Alignment(horizontal="center", vertical="center")
        BorTitulo = Border(left=Side(border_style= "thin"), right=Side(border_style= "thin"), bottom=Side(border_style= "thin"), top=Side(border_style= "thin"))
        FontTitulo = Font(name= "Calibri", size= 16 , bold=True)
        ws["A1:L1"].alignment = AlinTitulo
        ws["A1:L1"].border = BorTitulo
        ws["A1:L1"].font = FontTitulo
        ws["A1"]="Nombres"
        ws["B1"]="Apellidos"
        ws["C1"]="E-Mail"
        ws["D1"]="Curso"
        ws["E1"]="Procedencia"
        ws["F1"]="Matricula"
        ws["G1"]="Institucion"
        ws["H1"]="Estado"
        ws["I1"]="Pais"
        ws["J1"]="Municipio"
        ws["K1"]="Estado Civil"
        ws["L1"]="Carrera"
        fila=2
        co=1
        AlCont = Alignment(vertical="center")
        BoCont = Border(left=Side(border_style= "thin"), right=Side(border_style= "thin"), bottom=Side(border_style= "thin"), top=Side(border_style= "thin"))}
        FoCont = Font(name= "Calibri", size= 16)
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.nombres
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.apellidos
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.email
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.curso
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.procedencia
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.Matricula
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.Institucion
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.estado
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.pais
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.municipio
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.estadocivil
            fila +=1
        fila = 2
        co +=1
        for q in query:
            ws.cell(row=fila, column=col).alignment = AlCont
            ws.cell(row=fila, column=col).border = BoCont
            ws.cell(row=fila, column=col).font = FoCont 
            ws.cell(row=fila, column=col).value = q.Carrera
            fila +=1
        fila = 2
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter # Get the column name
            for cell in col:
                try: # Necessary to avoid error on empty cells
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width
        nombreArchivo="Reporte Pre-Registros.xlsx"
        response= HttpResponse(content_type="application/ms-excel")
        contenido = "attachment: filename = {0}".format(nombreArchivo)
        response["Content-Disposition"]= contenido
        wb.save(response)
        return response