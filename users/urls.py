from django.urls import path
from .views import CustomTokenObtainView, RegistroVista, ListaUsuariosVista, DetalleUsuarioVista, ActualizarUsuarioVista, EliminarUsuarioVista, UsuarioActualVista

urlpatterns = [
    path('registro/', RegistroVista.as_view(), name='registro'),
    path('usuarios/', ListaUsuariosVista.as_view(), name='lista-usuarios'),
    path('usuarios/<int:pk>/', DetalleUsuarioVista.as_view(), name='detalle-usuario'),
    path('usuarios/<int:pk>/actualizar/', ActualizarUsuarioVista.as_view(), name='actualizar-usuario'),
    path('usuarios/<int:pk>/eliminar/', EliminarUsuarioVista.as_view(), name='eliminar-usuario'),
    path('login/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('me/', UsuarioActualVista.as_view(), name='usuario_actual'),  
]
