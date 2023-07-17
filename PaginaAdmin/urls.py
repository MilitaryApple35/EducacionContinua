from django.urls import path
from .views import Login
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',Login,name='Login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)