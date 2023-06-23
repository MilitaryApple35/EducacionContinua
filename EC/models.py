from django.db import models

class Courses(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo


class Registro(models.Model):
    id= models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=50, blank=False)
    Apellidos = models.CharField(max_length=50, blank=False)
    Correo = models.CharField(max_length=320, blank=False)
    Curso = models.CharField(max_length=50, blank=False)
    Procedencia = models.CharField(max_length=50, blank=False)
    Matricula = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.titulo
