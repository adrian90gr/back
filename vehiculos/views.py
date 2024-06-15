from rest_framework import generics, permissions

from estaciones import serializers
from .models import Vehiculo
from .models import Usuario
from .serializers import VehiculoSerializer
from django.shortcuts import get_object_or_404

class ListaVehiculosVista(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        usuario_id = self.request.data.get('usuario')
        if usuario_id:
            usuario = get_object_or_404(Usuario, id=usuario_id)  # Asegúrate de importar el modelo Usuario
            serializer.save(usuario=usuario)
        else:
            raise serializers.ValidationError("El campo 'usuario' es obligatorio.")

class DetalleVehiculoVista(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'matricula'

class VehiculosPorUsuarioVista(generics.ListAPIView):
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Vehiculo.objects.filter(usuario__id=usuario_id)

# Nueva vista para búsqueda por matrícula
class VehiculoPorMatriculaVista(generics.RetrieveAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'matricula'