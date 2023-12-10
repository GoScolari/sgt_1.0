from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Notificacion, Vehiculo, Incidencia, Mantenimiento
from .forms import VehiculoForm, IncidenciaForm, MantenimientoForm
#from django.db.models import Q

# LOGIN
def inicio_sesion (request):
    return render(request, 'registration/login.html')
@login_required
def home (request):
    return render(request, 'seguimientoApp/index.html')
# RASTREO
def rastreo (request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/rastreo.html', {'vehiculos': vehiculos})
# PANEL
def panel(request):
    vehiculos = Vehiculo.objects.all()
    # Puedes agregar lógica adicional aquí para obtener datos de otras secciones como mantenimientos y personal
    
    return render(request, 'seguimientoApp/panel.html', {'vehiculos': vehiculos})

def salir (request):
    logout(request)
    return redirect('/')


# VEHICULOS
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/lista_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    return render(request, 'seguimientoApp/detalle_vehiculo.html', {'vehiculo': vehiculo})

def home(request):
    vehiculos = Vehiculo.objects.all()  # Asegúrate de importar el modelo Vehiculo
    return render(request, 'seguimientoApp/index.html', {'vehiculos': vehiculos})

def gestionar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'seguimientoApp/gestionar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_vehiculo.html', data)

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'seguimientoApp/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

def eliminar_vehiculo(request, vehiculo_id):
    # Obtener el vehículo
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        notificaciones_asociadas = Notificacion.objects.filter(incidencia__vehiculo=vehiculo)
        notificaciones_asociadas.delete()

        # Eliminar el vehículo
        vehiculo.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('gestionar_vehiculos')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_vehiculo.html', {'vehiculo': vehiculo})


# INCIDENCIAS
def lista_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'seguimientoApp/lista_incidencias.html', {'incidencias': incidencias})

def detalle_incidencia(request, incidencia_id):

    incidencia = get_object_or_404(Incidencia, pk=incidencia_id)
    return render(request, 'seguimientoApp/detalle_incidencia.html', {'incidencia': incidencia})

def gestionar_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'seguimientoApp/gestionar_incidencias.html', {'incidencias': incidencias})

def crear_incidencia(request):
    form = IncidenciaForm()
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')  # Reemplaza con el nombre correcto de la URL
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_incidencia.html', data)

def editar_incidencia(request, incidencia_id):
    incidencia = get_object_or_404(Incidencia, id=incidencia_id)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')
    else:
        form = IncidenciaForm(instance=incidencia)
    return render(request, 'seguimientoApp/editar_incidencia.html', {'form': form, 'incidencia': incidencia})

def eliminar_incidencia(request, incidencia_id):
    incidencia = Incidencia.objects.get(pk=incidencia_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        # notificaciones_asociadas = Notificacion.objects.filter(vehiculo=incidencia.vehiculo)
        # notificaciones_asociadas.delete()

        # Eliminar el vehículo
        incidencia.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('gestionar_incidencias')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_incidencia.html', {'incidencia': incidencia})

# MANTENCION

def mantencion(request):
    mantenimiento = Mantenimiento.objects.all()
    return render(request, 'seguimientoApp/mantencion.html', {'mantenimientos':mantenimiento})


def listar_mantencion(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'seguimientoApp/lista_mantencion.html', {'mantenimientos': mantenimientos})

def crear_mantencion(request):
    form = MantenimientoForm()
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mantencion')
    data = {'form': form}
    return render(request, 'seguimientoApp/crear_mantencion.html', data)

def editar_mantencion(request, mantencion_id):
    mantenimiento = get_object_or_404(Mantenimiento, id=mantencion_id)
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_mantencion')
    else:
        form = MantenimientoForm(instance=mantenimiento)
    return render(request, 'seguimientoApp/editar_mantencion.html', {'form': form, 'mantenimientos': mantenimiento})

def eliminar_mantencion(request, mantencion_id):
    # Obtener el vehículo
    mantenimiento = Mantenimiento.objects.get(pk=mantencion_id)

    if request.method == 'POST':
        # Verificar si hay notificaciones asociadas y eliminarlas
        # notificaciones_asociadas = Notificacion.objects.filter(incidencia__mantencion=mantenimiento)
        # notificaciones_asociadas.delete()

        # Eliminar el vehículo
        mantenimiento.delete()

        # Redirigir a alguna página después de la eliminación (puedes cambiar esto)
        return redirect('lista_mantencion')

    # Renderizar la confirmación de eliminación
    return render(request, 'seguimientoApp/eliminar_mantencion.html', {'mantenimientos': mantenimiento})