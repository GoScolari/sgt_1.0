from django.db import models

# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

# *************************

class Geolocalizacion(models.Model):
    geolocalizacion = models.CharField(max_length=50, blank=True, null=True)
    velocidad = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geolocalizacion'


class Incidencia(models.Model):
    fecha = models.DateField(blank=True, null=True)
    tipo_incidencia = models.CharField(max_length=50, blank=True, null=True)
    estado_incidencia = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    vehiculo = models.ForeignKey(
        'Vehiculo', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidencia'


class Mantenimiento(models.Model):
    tipo_mantenimiento = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    notas = models.CharField(max_length=60, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    personal = models.ForeignKey(
        'Personal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimiento'


class NotfPers(models.Model):
    # The composite primary key (notificacion_id, personal_id) found, that is not supported. The first column is selected.
    notificacion = models.ForeignKey(
        'Notificacion', on_delete=models.CASCADE)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notf_pers'
        unique_together = (('notificacion', 'personal'),)


class Notificacion(models.Model):
    fecha = models.DateField(blank=True, null=True)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    incidencia = models.ForeignKey(
        Incidencia, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class Personal(models.Model):
    rut = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_p = models.CharField(max_length=50, blank=True, null=True)
    apellido_m = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contraseña = models.CharField(max_length=50, blank=True, null=True)
    rol = models.ForeignKey('Rol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'
    
    def __str__(self):
        return self.nombre + " " + self.apellido_p


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    rut = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Repuesto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    proveedor = models.ForeignKey(
        Proveedor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repuesto'


class Rol(models.Model):
    cargo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RptoMtto(models.Model):
    # The composite primary key (repuesto_id, mantenimiento_id) found, that is not supported. The first column is selected.
    repuesto = models.OneToOneField(
        Repuesto, models.DO_NOTHING, primary_key=True)
    mantenimiento = models.ForeignKey(Mantenimiento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rpto_mtto'
        unique_together = (('repuesto', 'mantenimiento'),)


# class TipoVehiculo(models.Model):
#     tipo_vehiculo = models.CharField(max_length=50, blank=True, null=True)
#     descripcion = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tipo_vehiculo'

# models.py

class TipoVehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'

    def __str__(self):
        return self.tipo_vehiculo



class Vehiculo(models.Model):
    numero_ppu = models.CharField(max_length=6, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    num_chasis = models.IntegerField(blank=True, null=True)
    ano_fabricacion = models.DateField(blank=True, null=True)
    kilometraje = models.FloatField(blank=True, null=True)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    tipo_vehiculo = models.ForeignKey(
        TipoVehiculo, models.DO_NOTHING, blank=True, null=True)
    geolocalizacion = models.ForeignKey(
        Geolocalizacion, models.DO_NOTHING, blank=True, null=True)
    mantenimiento = models.ForeignKey(
        Mantenimiento, models.DO_NOTHING, blank=True, null=True)
    personal = models.ForeignKey(
        Personal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'
    
    def __str__(self):
        return self.numero_ppu
