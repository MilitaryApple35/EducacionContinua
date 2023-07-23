# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs de tu aplicación
    path('', views.login_view, name='login'),
    path('administracion/', views.administracion, name='administracion'),
]

