from django.contrib import admin
from .models import Productos, Proveedores

admin.site.register(Proveedores)
admin.site.register(Productos)
