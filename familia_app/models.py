from unittest.util import _MAX_LENGTH
from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    grado_consanguineo = models.IntegerField()
    fecha_cumpleaños = models.DateField()

    def __str__ (self):
        return f"{self.nombre} - {self.parentezco} - {self.grado_consanguineo} - {self.fecha_cumpleaños}"