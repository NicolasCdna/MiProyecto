from django.shortcuts import render, redirect 
from .forms import VehiculoForm 

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
            return redirect('vehiculo_list')  # Redirige a una vista que lista los vehículos
    else:
        form = VehiculoForm()
    return render(request, 'crear_vehiculo.html', {'form': form})
