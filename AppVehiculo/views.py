from django.shortcuts import render, redirect 
from .forms import VehiculoForm 
from .models import Vehiculo
from .forms import VersionForm
from .models import Version
from .forms import ProxyForm
from .models import Proxy


# Create your views here.
def index(request):
    context = {
        'titulo': 'Inicio',
        'mensaje': 'Bienvenido a la página de inicio'
    }
    return render(request, 'AppVehiculo/index.html',context)


def crear_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')  # Redirige a una vista que lista los vehículos
    else:
        form = VehiculoForm()
    return render(request, 'AppVehiculo/crear_vehiculo.html', {'form': form})

# Para listar los vehiculos
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'AppVehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})


##VERSION
def agregar_version(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_versiones')  # Redirige a la lista de versiones o a otra página
    else:
        form = VersionForm()
    return render(request, 'AppVehiculo/agregar_version.html', {'form': form})

#Lista de Versiones:
def lista_versiones(request):
    versiones = Version.objects.all()
    return render(request, 'AppVehiculo/lista_versiones.html', {'versiones': versiones})

#Crear Proxy
def crear_proxy(request):
    if request.method == 'POST':
        form = ProxyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proxies')  # Redirige a una lista de proxies o similar
    else:
        form = ProxyForm()
    return render(request, 'AppVehiculo/crear_proxy.html', {'form': form})
#Lista de Proxies
def lista_proxies(request):
    proxies = Proxy.objects.all()
    return render(request, 'AppVehiculo/lista_proxies.html', {'proxies': proxies})