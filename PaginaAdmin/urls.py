from django.urls import path
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
