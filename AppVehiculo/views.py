from django.shortcuts import render, redirect 
from .forms import VehiculoForm 
from .models import Vehiculo

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
