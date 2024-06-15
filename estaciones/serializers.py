from rest_framework import serializers
from .models import Estacion
import base64

class EstacionSerializer(serializers.ModelSerializer):
    foto = serializers.SerializerMethodField()

    class Meta:
        model = Estacion
        fields = ['id', 'nombre', 'latitud', 'longitud', 'npuntoscarga', 'fecha_construccion', 'foto']

    def get_foto(self, obj):
        if obj.foto:
            return base64.b64encode(obj.foto).decode('utf-8')
        return None

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if 'foto' in request.FILES:
            instance.foto = request.FILES['foto'].read()
        elif 'eliminarFoto' in request.data and request.data['eliminarFoto'] == 'true':
            instance.foto = None

        return super().update(instance, validated_data)

class RegistroEstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = ['nombre', 'latitud', 'longitud', 'npuntoscarga', 'fecha_construccion', 'foto']

    def create(self, validated_data):
        request = self.context.get('request')
        foto = None
        if 'foto' in request.FILES:
            foto = request.FILES['foto'].read()

        estacion = Estacion(
            nombre=validated_data['nombre'],
            latitud=validated_data['latitud'],
            longitud=validated_data['longitud'],
            npuntoscarga=validated_data.get('npuntoscarga'),
            fecha_construccion=validated_data.get('fecha_construccion'),
            foto=foto
        )
        estacion.save()
        return estacion
