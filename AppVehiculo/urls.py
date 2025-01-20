from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
]
