from rest_framework import generics, permissions
from .models import Valoracion
from .serializers import ValoracionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

class ListaValoracionesVista(generics.ListCreateAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetalleValoracionVista(generics.RetrieveAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActualizarValoracionVista(generics.UpdateAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]

class EliminarValoracionVista(generics.DestroyAPIView):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ValoracionesPorUsuarioVista(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, usuario_id):
        valoraciones = Valoracion.objects.filter(usuario_id=usuario_id)
        serializer = ValoracionSerializer(valoraciones, many=True)
        return Response(serializer.data)

class ValoracionesPorEstacionVista(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, estacion_id):
        valoraciones = Valoracion.objects.filter(estacion_id=estacion_id)
        serializer = ValoracionSerializer(valoraciones, many=True)
        return Response(serializer.data)



class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)