from django.db import models

class Courses(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo

class Conferencias(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo

class Talleres(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo

class Diplomados(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo

class Congresos(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo
    
class Capacitaciones(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo

class Registro(models.Model):
    id= models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    tipoRegistro = models.CharField(max_length=25)
    curso = models.CharField(max_length=100)
    procedencia = models.CharField(max_length=50)
    Matricula = models.CharField(max_length=50, blank=True)
    Institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=15)
    Carrera = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


