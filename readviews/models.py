from django.db import models

class datos_generales(models.Model):
    titulo = models.TextField(max_length=80)
    fecha_inicio = models.DateField()
    tipo = models.TextField(max_length=10)
    comentarios = models.TextField(100)
    autor = models.TextField(40)

class serie(datos_generales):
    temporadas = models.IntegerField()
    plataforma = models.TextField(max_length=30)
    fecha_final = models.DateField()

class pelicula(datos_generales):
    fecha_final = datos_generales.fecha_inicio
    plataforma = models.TextField(max_length=30)
    genero = models.TextField(max_length=20)

class libro(datos_generales):
    fecha_final = models.DateField()
    genero = models.TextField(max_length=25)

    
