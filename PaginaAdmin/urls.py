from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from PaginaAdmin import views

urlpatterns = [
    # Otras URLs de tu aplicación
    path('login/', views.login_view, name='login'),
    path('administracion/', views.administracion, name='administracion'),
]
