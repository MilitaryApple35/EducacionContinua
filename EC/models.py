from django.db import models

class Courses(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='cajas/', blank=False)
    titulo = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False)
    
    def __str__(self):
        return self.titulo
