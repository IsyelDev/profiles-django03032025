from rest_framework import serializers
from cursos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto  # Sin comillas, debe ser la referencia directa al modelo
        fields = "__all__"  # "__all__" debe ir en minúsculas
