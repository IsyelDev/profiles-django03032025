from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=100,null=True,blank=True)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    precio=models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-precio"]
        
        
    def __str__(self):
       return f"{self.nombre} ,{self.precio:,.2f}" 

