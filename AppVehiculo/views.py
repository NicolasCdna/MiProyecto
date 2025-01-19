from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': 'Inicio',
        'mensaje': 'Bienvenido a la página de inicio'
    }
    return render(request, 'AppVehiculo/index.html',context)