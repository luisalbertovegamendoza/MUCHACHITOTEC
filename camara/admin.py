from django.contrib import admin
from .models import Producto , Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(Producto)

class ProductAdmin(admin.ModelAdmin):
    list_display =(
        'id' ,
        'nombre' ,
        'detalle',
        'precio',
        'imagen',
    )
    
    list_filter = ('category',)
    search_fields = ('nombre',)

   


