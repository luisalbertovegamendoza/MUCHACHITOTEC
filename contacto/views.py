from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import MensajeContacto

@csrf_protect
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        telefono = request.POST.get('telefono', '').strip()  # <--- nuevo

        mensaje = request.POST.get('mensaje', '').strip()

        if not nombre or not email or not telefono or not mensaje:
            messages.error(request, "Todos los campos del contacto son obligatorios")
            return redirect('index')

        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            mensaje=mensaje
        )

        messages.success(request, "Mensaje enviado correctamente 📩")
        return redirect('index')

    return redirect('index')


    
