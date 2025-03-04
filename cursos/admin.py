from django.contrib import admin
from cursos.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "cantidad")
    search_fields = ("nombre", "descripcion")  # Permite buscar productos
    list_filter = ("cantidad",)  # Agrega filtros por cantidad
    ordering = ("nombre",)  # Ordena los productos alfabéticamente
