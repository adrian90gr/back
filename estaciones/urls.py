from django.urls import path
from .views import (RegistroEstacionVista, ListaEstacionesVista,DetalleEstacionVista,ActualizarEstacionVista,
EliminarEstacionVista)


urlpatterns = [
    path('registrar/', RegistroEstacionVista.as_view(), name='registrar-estacion'),
    path('', ListaEstacionesVista.as_view(), name='lista-estaciones'),
    path('<int:pk>/', DetalleEstacionVista.as_view(), name='detalle-estacion'),
    path('<int:pk>/actualizar/', ActualizarEstacionVista.as_view(), name='actualizar-estacion'),  
    path('<int:pk>/eliminar/', EliminarEstacionVista.as_view(), name='eliminar-estacion'),       
]

