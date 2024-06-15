from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import EstacionSerializer, RegistroEstacionSerializer
from .models import Estacion

class RegistroEstacionVista(generics.CreateAPIView):
    queryset = Estacion.objects.all()
    serializer_class = RegistroEstacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListaEstacionesVista(generics.ListAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetalleEstacionVista(generics.RetrieveAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActualizarEstacionVista(generics.UpdateAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class EliminarEstacionVista(generics.DestroyAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    permission_classes = [permissions.IsAuthenticated]
