from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
import base64

class UsuarioSerializer(serializers.ModelSerializer):
    foto = serializers.SerializerMethodField()
    contraseña = serializers.CharField(write_only=False, required=False)  

    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'nombre', 'apellidos', 'telefono', 'foto', 'admin', 'contraseña']

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

        if 'contraseña' in validated_data:
            instance.set_password(validated_data['contraseña'])
            validated_data.pop('contraseña', None)
        return super().update(instance, validated_data)


class RegistroSerializer(serializers.ModelSerializer):
    contraseña = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'apellidos', 'telefono', 'foto', 'contraseña', 'admin']

    def create(self, validated_data):
        usuario = Usuario(
            correo=validated_data['correo'],
            nombre=validated_data['nombre'],
            apellidos=validated_data['apellidos'],
            telefono=validated_data['telefono'],
            foto=validated_data.get('foto', None),
            admin=validated_data.get('admin', False)
        )
        usuario.set_password(validated_data['contraseña'])
        usuario.save()
        return usuario
    


class CustomTokenObtainSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contraseña = serializers.CharField(write_only=True)

    def validate(self, attrs):
        correo = attrs.get('correo')
        contraseña = attrs.get('contraseña')

        user = authenticate(request=self.context.get('request'), correo=correo, password=contraseña)

        if not user:
            raise serializers.ValidationError('Credenciales incorrectas')

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'correo': user.correo,
            'nombre': user.nombre,
            'admin': user.admin,
        }
