from django.db import models
import datetime
from django.conf import settings
# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=20)
    creditos = models.PositiveSmallIntegerField()
    fecha = models.DateField(auto_now_add=True)


    def __str__(self):

        texto = '{0} ({1})'
        return texto.format(self.nombre, self.creditos)
        # return (f"{self.nombre}, {self.fecha}")