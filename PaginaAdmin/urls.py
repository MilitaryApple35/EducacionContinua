# urls.py
from django.urls import path
from . import views
from PaginaAdmin import views
from django.contrib.auth import views as auth_views
from .views import agregarCurso
from django.conf.urls.static import static
from django.conf import settings
from .views import agregarCurso, ReporteCursosExcel, ReporteCapacitacionesExcel, ReporteConferenciasExcel, ReporteCongresosExcel, ReporteDiplomadosExcel, ReporteTalleresExcel
from .views import *


urlpatterns = [
    # Otras URLs de tu aplicación
    path('', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('editar-curso/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('eliminar-curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('agregar-curso/',agregarCurso,name='agregarCurso'),
    path('agregar-conferencia/',agregarConferencia,name='agregarConferencia'),
    path('editar-conferencia/<int:conferencia_id>/', views.editar_conferencia, name='editar_conferencia'),
    path('eliminar-conferencia/<int:conferencia_id>/', views.eliminar_conferencia, name='eliminar_conferencia'),
    path('agregar-taller/',agregarTaller,name='agregarTaller'),
    path('editar-taller/<int:taller_id>/', views.editar_taller, name='editar_taller'),
    path('eliminar-taller/<int:taller_id>/', views.eliminar_taller, name='eliminar_taller'),
    path('agregar-diplomado/', views.agregarDiplomado, name='agregarDiplomado'),
    path('editar-diplomado/<int:diplomado_id>/', views.editar_diplomado, name='editar_diplomado'),
    path('eliminar-diplomado/<int:diplomado_id>/', views.eliminar_diplomado, name='eliminar_diplomado'),
    path('agregar-congreso/', views.agregarCongreso, name='agregarCongreso'),
    path('editar-congreso/<int:congreso_id>/', views.editar_congreso, name='editar_congreso'),
    path('eliminar-congreso/<int:congreso_id>/', views.eliminar_congreso, name='eliminar_congreso'),
    path('agregar-capacitacion/', views.agregarCapacitacion, name='agregarCapacitacion'),
    path('editar-capacitacion/<int:capacitacion_id>/', views.editar_capacitacion, name='editar_capacitacion'),
    path('eliminar-capacitacion/<int:capacitacion_id>/', views.eliminar_capacitacion, name='eliminar_capacitacion'),
    path('',auth_views.LogoutView.as_view(next_page='login.html'), name='logout'),
    path('reporte-talleres/', ReporteTalleresExcel.as_view(), name='reporteTalleres'),
    path('reporte-cursos/', ReporteCursosExcel.as_view(), name='reporteCursos'),
    path('reporte-capacitaciones/', ReporteCapacitacionesExcel.as_view(), name='reporteCapacitaciones'),
    path('reporte-conferencias/', ReporteConferenciasExcel.as_view(), name='reporteConferencias'),
    path('reporte-congresos/', ReporteCongresosExcel.as_view(), name='reporteCongresos'),
    path('reporte-diplomados/', ReporteDiplomadosExcel.as_view(), name='reporteDiplomados'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ARREGLAR ESTO
"""""
from django.conf.urls.static import static
from django.conf import settings
from PaginaAdmin import views
from .views import agregarCurso
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Otras URLs de tu aplicación
    path('',agregarCurso,name='agregarCurso'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('administracion/', views.administracion, name='administracion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""