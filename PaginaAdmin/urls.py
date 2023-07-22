from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from PaginaAdmin import views
from .views import agregarCurso

urlpatterns = [
    # Otras URLs de tu aplicación
    path('login/', views.login_view, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('',agregarCurso,name='agregarCurso'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
