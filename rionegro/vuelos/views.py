from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

# Vista para la página de inicio
def home(request):
    return render(request, 'vuelos/home.html')

# Vista para registrar un vuelo
def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el vuelo en la base de datos
            return redirect('listar_vuelos')  # Redirigimos a la vista de listar vuelos
    else:
        form = FlightForm()  # Si no es POST, mostramos un formulario vacío
    return render(request, 'vuelos/registrar_vuelo.html', {'form': form})

# Vista para listar los vuelos
def listar_vuelos(request):
    vuelos = Flight.objects.all().order_by('price')  # Obtenemos todos los vuelos ordenados por precio
    return render(request, 'vuelos/listar_vuelos.html', {'vuelos': vuelos})

# Vista para mostrar las estadísticas de los vuelos
def estadisticas_vuelos(request):
    vuelos_nacionales = Flight.objects.filter(tipo='Nacional').count()  # Contamos los vuelos nacionales
    vuelos_internacionales = Flight.objects.filter(tipo='Internacional').count()  # Contamos los vuelos internacionales
    precio_promedio_nacional = Flight.objects.filter(tipo='Nacional').aggregate(Avg('price'))['price__avg']  # Calculamos el precio promedio de los vuelos nacionales
    return render(request, 'vuelos/estadisticas_vuelos.html', {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'precio_promedio_nacional': precio_promedio_nacional,
    })
