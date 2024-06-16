from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('users.urls')),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('/estaciones/', include('estaciones.urls')), 
    path('/vehiculos/', include('vehiculos.urls')),  
    path('/valoraciones/', include('valoraciones.urls')), 
]