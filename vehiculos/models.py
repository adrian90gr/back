from django.db import models
from users.models import Usuario

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='vehiculos')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio=models.IntegerField(null=True)
    categoria = models.CharField(max_length=20, default='DefaultCategoria') 

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula} {self.anio})"
