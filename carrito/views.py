from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .carrito import Carrito
from django.urls import reverse
from camara.models import Producto
from django.shortcuts import render, redirect
from django.urls import reverse
from .carrito import Carrito
from camara.models import Producto
from JJTECNOLOGIAEIRL import paypal_config
import paypalrestsdk
from django.contrib import messages # mostrar mensajes en django


# ------------------- Funciones del carrito -------------------

def agregar_carrito(request, producto_id):

    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto)

    messages.success(request, 'Producto agregado al carrito')
    return redirect('carrito:ver_carrito')



def restar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    return redirect('carrito:ver_carrito')

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito:ver_carrito')



def ver_carrito(request):
    carrito = request.session.get('carrito', {})

    # Calculamos el subtotal de cada producto
    for key, item in carrito.items():
        item['subtotal'] = float(item['precio']) * item['cantidad']

    # Calculamos el total general
    total = sum(item['subtotal'] for item in carrito.values())

    return render(request, 'carrito/carrito.html', {'carrito': carrito, 'total': total})


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito:ver_carrito')

# ------------------- PayPal Checkout -------------------

def pagar_paypal(request):
    carrito = request.session.get('carrito', {})
    total = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())

    # 🧮 PayPal solo usa USD, así que si tus precios están en soles,
    # puedes convertirlos (ejemplo: 1 USD = 3.8 PEN)
    total_usd = round(total / 3.8, 2)

    pago = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('carrito:pago_exitoso')),
            "cancel_url": request.build_absolute_uri(reverse('carrito:pago_cancelado')),
        },
        "transactions": [{
            "item_list": {
                "items": [
                    {
                        "name": "Compra en JJ TECNOLOGIA",
                        "sku": "001",
                        "price": str(total_usd),
                        "currency": "USD",
                        "quantity": 1,
                    }
                ]
            },
            "amount": {
                "total": str(total_usd),
                "currency": "USD"
            },
            "description": "Compra en JJ TECNOLOGIA (pago en línea)"
        }]
    })

    if pago.create():
        for link in pago.links:
            if link.rel == "approval_url":
                return redirect(link.href)
        return HttpResponse("Error: No se encontró la URL de aprobación de PayPal.")
    else:
        return HttpResponse("Error al crear el pago con PayPal.")
    
def pago_exitoso(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'carrito/pago_exitoso.html')

def pago_cancelado(request):
    return render(request, 'carrito/pago_cancelado.html')




def pagar_yape(request):
    total = request.GET.get('total', 0)  # Obtenemos el total enviado desde el carrito
    return render(request, "carrito/yape.html", {'total': total})
