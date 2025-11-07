from django.contrib import admin
from .models import Empleados, Clientes, Servicios

admin.site.register(Empleados)
admin.site.register(Clientes)
admin.site.register(Servicios)