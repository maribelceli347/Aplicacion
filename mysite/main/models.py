from django.db import models

# Create your models here.
class Veterinaria(models.Model):
    veterinaria_nombre = models.CharField(max_length=200)
    veterinaria_direcion = models.CharField(max_length=200)
    veterinaria_descripcion = models.TextField()
    veterinaria_creacion = models.DateTimeField("fecha de Publicacion")

    def __str__(self):
        return self.veterinaria_nombre


