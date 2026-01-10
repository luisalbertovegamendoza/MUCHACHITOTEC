

from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static # IMAGENES
from django.conf import settings          



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # APPS
    path('camara/', include('camara.urls')),
    path('carrito/', include('carrito.urls')),
    # USUARIOS
    path('login/', views.login_usuario , name='login'),
    path('logout/', views.logout_usuario,name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('contacto/', include('contacto.urls')),
    path('chatbot/', include('chatbot.urls')),

    
    


    


    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)