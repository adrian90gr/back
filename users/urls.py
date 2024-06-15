from django.urls import path
from .views import CustomTokenObtainView, RegistroVista, ListaUsuariosVista, DetalleUsuarioVista, ActualizarUsuarioVista, EliminarUsuarioVista, UsuarioActualVista

urlpatterns = [
    path('registro/', RegistroVista.as_view(), name='registro'),
    path('users/', ListaUsuariosVista.as_view(), name='lista-usuarios'),
    path('users/<int:pk>/', DetalleUsuarioVista.as_view(), name='detalle-usuario'),
    path('users/<int:pk>/actualizar/', ActualizarUsuarioVista.as_view(), name='actualizar-usuario'),
    path('users/<int:pk>/eliminar/', EliminarUsuarioVista.as_view(), name='eliminar-usuario'),
    path('login/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('me/', UsuarioActualVista.as_view(), name='usuario_actual'),  
]
