from sqlite3 import Cursor
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class LenguajeM(models.Model):
    Nom_Leng = models.CharField(max_length=20)
    Historia = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.Nom_Leng

    def get_absolute_url(self):
        return reverse("lenguaje_detalle", args=[str(self.id)])


class Course(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=300)
    Creador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    Año_Experiencia = models.PositiveIntegerField()
    Lenguaje = models.ForeignKey(
        LenguajeM, on_delete=models.CASCADE, related_name='Lenguajes',)
    Horas = models.PositiveIntegerField()
    Link_Cont = models.URLField(
        null=True, blank=True, verbose_name="Dirección Web")
    Fecha_Creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Nombre

    def get_absolute_url(self):
        return reverse("cursos_detalle", args=[str(self.id)])


class Comentarios(models.Model):
    Curso = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='comentarios',)
    Comentario = models.CharField(max_length=200)
    NombreU = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.Comentario

    def get_absolute_url(self):
        return reverse("cursos_detalle", args=[str(self.Curso_id)])
