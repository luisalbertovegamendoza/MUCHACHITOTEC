from django.db import models
from cloudinary.models import CloudinaryField



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    

class Producto(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productos')    
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    imagen = CloudinaryField('imagen', blank=True, null=True)

    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        


    def __str__(self):
        return self.nombre