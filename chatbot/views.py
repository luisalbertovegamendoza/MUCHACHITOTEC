from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from camara.models import Producto


WHATSAPP_NUMERO = "51933470244"
TELEFONO = "+51933470244"


# MENÚ
MENU = {
    "1": "productos",
    "2": "envios",
    "3": "pagos",
    "4": "horarios",
    "5": "contacto",
}

RESPUESTAS = {
    "envios": "🚚 Realizamos envíos a todo el peru",
    "pagos": "💳 Aceptamos Yape, Plin, tarjetas y transferencias.",
    "horarios": "⏰ Atendemos de lunes a domingo de 9am a 7pm.",
    "contacto": (
    "📞 <b>¿Cómo deseas contactarnos?</b><br><br>"
    f"<a href='https://wa.me/{WHATSAPP_NUMERO}?text=Hola,%20vengo%20del%20chatbot' "
    "target='_blank' style='color:green;font-weight:bold;'>"
    "💬 WhatsApp</a><br><br>"
    f"<a href='tel:{TELEFONO}' "
    "style='color:blue;font-weight:bold;'>"
    "📞 Llamar ahora</a>"
)
}

# CONTEXTO SIMPLE EN MEMORIA
CONTEXTO = {}

def buscar_productos(texto):
    productos = Producto.objects.filter(
        nombre__icontains=texto,
        disponible=True
    )[:3]

    if productos.exists():
        respuesta = "🛒 <b>Productos encontrados:</b><br><br>"
        for p in productos:
            respuesta += f"""
            🔹 <b>{p.nombre}</b><br>
            💲 S/ {p.precio}<br><br>
            """
        respuesta += (
            "📲 <b>¿Deseas ayuda para comprar?</b><br>"
            f"<a href='https://wa.me/{WHATSAPP_NUMERO}?text=Hola,%20quiero%20información%20del%20producto' "
            "target='_blank'>💬 WhatsApp</a>"
        )

        return respuesta

    return (
        "😕 No encontré productos con ese nombre.<br><br>"
        "📲 <a href='https://wa.me/51933470244' target='_blank'>Hablar con un asesor</a>"
    )

@csrf_exempt
def chatbot_respuesta(request):
    if request.method != "POST":
        return JsonResponse({"respuesta": "Método no permitido"})

    data = json.loads(request.body)
    mensaje = data.get("mensaje", "").lower().strip()
    usuario = request.META.get("REMOTE_ADDR")  # identifica usuario

    # 📌 Selección por número
    if mensaje in MENU:
        opcion = MENU[mensaje]
        CONTEXTO[usuario] = opcion

        if opcion == "productos":
            return JsonResponse({
                "respuesta": "🛒 Perfecto, dime qué producto buscas."
            })

        return JsonResponse({
            "respuesta": RESPUESTAS[opcion]
        })

    # 📌 Si está en modo productos → buscar
    if CONTEXTO.get(usuario) == "productos":
        return JsonResponse({
            "respuesta": buscar_productos(mensaje)
        })

    # 📌 Palabras clave directas
    for key, texto in RESPUESTAS.items():
        if key in mensaje:
            return JsonResponse({"respuesta": texto})

    # 📌 Respuesta por defecto
    return JsonResponse({
        "respuesta": (
            "🤔 No entendí tu mensaje.<br><br>"
            "1️⃣ Productos<br>"
            "2️⃣ Envíos<br>"
            "3️⃣ Pagos<br>"
            "4️⃣ Horarios<br>"
            "5️⃣ Contacto"
        )
    })
