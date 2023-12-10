from django.urls import path
from .views import *
# lista_vehiculos, detalle_vehiculo, gestionar_vehiculos, crear_vehiculo, editar_vehiculo, eliminar_vehiculo, lista_incidencias, detalle_incidencia, gestionar_incidencias, crear_incidencia, editar_incidencia, eliminar_incidencia


urlpatterns = [
    path('lista_vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('detalle_vehiculo/<int:vehiculo_id>/', detalle_vehiculo, name='detalle_vehiculo'),
    path('gestionar_vehiculos/', gestionar_vehiculos, name='gestionar_vehiculos'),
    path('vehiculos/crear/', crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:vehiculo_id>/', editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', eliminar_vehiculo, name='eliminar_vehiculo'),

    path('crear_incidencia/', crear_incidencia, name='crear_incidencia'),
    path('lista_incidencias/', lista_incidencias, name='lista_incidencias'),
    path('detalle_incidencia/<int:incidencia_id>/', detalle_incidencia, name='detalle_incidencia'),
    path('gestionar_incidencias/', gestionar_incidencias, name='gestionar_incidencias'),
    path('editar_incidencia/<int:incidencia_id>/', editar_incidencia, name='editar_incidencia'),
    path('eliminar_incidencia/<int:incidencia_id>/', eliminar_incidencia, name='eliminar_incidencia'),

    path('mantencion/', mantencion, name='mantencion'),
    path('lista_mantencion/', listar_mantencion, name='lista_mantencion'),  
    path('crear_mantencion/', crear_mantencion , name='crear_mantencion'),
    path('editar/<int:mantencion_id>/', editar_mantencion, name='editar_mantencion'),
    path('eliminar/<int:mantencion_id>/', eliminar_mantencion, name='eliminar_mantencion'),
    # Agrega más rutas para crear, actualizar, eliminar, etc.
]
