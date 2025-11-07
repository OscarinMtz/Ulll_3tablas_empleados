from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleados
import random

def inicio_spa(request):
    return render(request, 'inicio.html')

def agregar_empleado(request):
    if request.method == 'POST':
        # Generar ID de servicios automáticamente (1-10)
        id_servicios_auto = random.randint(1, 10)
        
        # Procesar datos del formulario sin forms.py
        empleado = Empleados(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            especialidad=request.POST['especialidad'],
            telefono=request.POST['telefono'],
            cargo=request.POST['cargo'],
            id_servicios=id_servicios_auto  # Se asigna automáticamente
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleados/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id_empleados=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.especialidad = request.POST['especialidad']
        empleado.telefono = request.POST['telefono']
        empleado.cargo = request.POST['cargo']
        # No actualizamos id_servicios para mantenerlo automático
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleados/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id_empleados=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})