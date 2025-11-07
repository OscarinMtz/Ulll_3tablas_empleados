from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_spa, name='inicio_spa'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
]