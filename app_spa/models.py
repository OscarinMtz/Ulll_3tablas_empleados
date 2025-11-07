from django.db import models

# ==========================================
# MODELO: Empleados
# ==========================================
class Empleados(models.Model):
    id_empleados = models.AutoField(primary_key=True)  # ¡Esto hace que sea automático!
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    cargo = models.CharField(max_length=100)
    id_servicios = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ... (los otros modelos permanecen igual)
# ==========================================
# MODELO: Clientes
# ==========================================
class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    alergias = models.TextField(blank=True, null=True)
    preferencias = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Servicios
# ==========================================
class Servicios(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField(help_text="Duración en minutos")
    tipo_servicio = models.CharField(max_length=100)
    id_clientes = models.IntegerField(default=1)  # Valor por defecto
    
    def __str__(self):
        return self.nombre