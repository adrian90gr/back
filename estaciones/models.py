from django.db import models

class Estacion(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    latitud = models.CharField(max_length=20, verbose_name="Latitud")
    longitud = models.CharField(max_length=20, verbose_name="Longitud")
    npuntoscarga = models.SmallIntegerField()
    fecha_construccion = models.DateField()
    foto = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.nombre
