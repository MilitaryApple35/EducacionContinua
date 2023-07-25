# urls.py
from django.urls import path
from . import views
from PaginaAdmin import views
from django.contrib.auth import views as auth_views
from .views import agregarCurso
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Otras URLs de tu aplicación
    path('', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('editar-curso/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('eliminar-curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('agregar-curso/',agregarCurso,name='agregarCurso'),
    path('',auth_views.LogoutView.as_view(next_page='login.html'), name='logout'),
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