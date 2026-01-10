

# Register your models here.
from django.contrib import admin
from .models import MensajeContacto



@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email','telefono', 'mensaje_corto', 'fecha')
    search_fields = ('nombre', 'email', 'mensaje')
    list_filter = ('fecha',)

    def mensaje_corto(self, obj):
        return obj.mensaje[:50] + "..." if len(obj.mensaje) > 50 else obj.mensaje
    mensaje_corto.short_description = 'Mensaje'
