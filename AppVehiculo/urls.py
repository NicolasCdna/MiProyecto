from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('lista_versiones/', views.lista_versiones, name='lista_versiones'),
    path('agregar_version/', views.agregar_version, name='agregar_version'),
    path('crear-proxy/', views.crear_proxy, name='crear_proxy'),
    path('lista-proxies/', views.lista_proxies, name='lista_proxies'),
]
