from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class GestorUsuarios(BaseUserManager):
    def create_user(self, correo, contraseña=None, **extra_fields):
        if not correo:
            raise ValueError('El campo correo debe estar establecido')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(contraseña)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contraseña=None, **extra_fields):
        extra_fields.setdefault('admin', True)
        return self.create_user(correo, contraseña, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, unique=True) 
    foto = models.BinaryField(null=True, blank=True)
    admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_permissions_set',  
        blank=True
    )

    objects = GestorUsuarios()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'telefono']

    def __str__(self):
        return self.correo
