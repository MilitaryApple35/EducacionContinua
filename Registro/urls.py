from django.urls import path
from .views import register
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',register,name='Registro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
