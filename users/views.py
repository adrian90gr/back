from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.response import Response
from rest_framework.views import APIView  
from rest_framework.permissions import IsAuthenticated 
from .serializers import CustomTokenObtainSerializer, RegistroSerializer, UsuarioSerializer
from .models import Usuario

class CustomTokenObtainView(TokenViewBase):
    serializer_class = CustomTokenObtainSerializer

class RegistroVista(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

class ListaUsuariosVista(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetalleUsuarioVista(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActualizarUsuarioVista(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

class EliminarUsuarioVista(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioActualVista(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
