from django.db import models
from users.models import Usuario
from estaciones.models import Estacion

class Valoracion(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateTimeField(null=True)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='valoraciones')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'Valoración {self.id} - {self.puntuacion}'
