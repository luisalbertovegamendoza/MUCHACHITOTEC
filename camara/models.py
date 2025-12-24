from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class Producto(models.Model):
    
    
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    imagen=models.ImageField(upload_to='empleado' , blank=True , null=True)
    
   

    def __str__(self):
        return self.nombre