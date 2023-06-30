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
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Email = models.EmailField( max_length=254)
    Curso = models.CharField(max_length=50)
    Procedencia = models.CharField(max_length=50)
    Matricula = models.CharField(max_length=50, blank=True)
    Institucion = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    Municipio = models.CharField(max_length=50)
    EstadoCivil = models.CharField(max_length=15)

    def __str__(self):
        return self.titulo
