from django.urls import path
from .views import (ListaValoracionesVista, DetalleValoracionVista, ValoracionesPorUsuarioVista, ValoracionesPorEstacionVista, ActualizarValoracionVista, EliminarValoracionVista)

urlpatterns = [
    path('', ListaValoracionesVista.as_view(), name='lista-valoraciones'),
    path('registrar/', ListaValoracionesVista.as_view(), name='registrar-valoracion'),
    path('<int:pk>/', DetalleValoracionVista.as_view(), name='detalle-valoracion'),
    path('<int:pk>/actualizar/', ActualizarValoracionVista.as_view(), name='actualizar-valoracion'),
    path('<int:pk>/eliminar/', EliminarValoracionVista.as_view(), name='eliminar-valoracion'),
    path('usuario/<int:usuario_id>/', ValoracionesPorUsuarioVista.as_view(), name='valoraciones-por-usuario'),
    path('estacion/<int:estacion_id>/', ValoracionesPorEstacionVista.as_view(), name='valoraciones-por-estacion'),
]
