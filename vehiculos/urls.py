from django.urls import path
from .views import ListaVehiculosVista, DetalleVehiculoVista, VehiculosPorUsuarioVista, VehiculoPorMatriculaVista

urlpatterns = [
    path('', ListaVehiculosVista.as_view(), name='lista-vehiculos'),
    path('<str:matricula>/', DetalleVehiculoVista.as_view(), name='detalle-vehiculo'),
    path('usuario/<int:usuario_id>/', VehiculosPorUsuarioVista.as_view(), name='vehiculos-por-usuario'),
    path('matricula/<str:matricula>/', VehiculoPorMatriculaVista.as_view(), name='vehiculo-por-matricula'),
]
