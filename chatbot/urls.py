from django.urls import path
from .views import chatbot_respuesta

urlpatterns = [
    path('responder/', chatbot_respuesta, name='chatbot'),
]
