from django.db import models

class Genero(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default = False)

class Author(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    alias = models.CharField(max_length=50)

class ShortStories(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    estado = models.BooleanField(default = False)
    texto = models.CharField(max_length=100)
