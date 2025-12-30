from django.urls import path
from .views import ProductosPorCategoriaListView, ProductoDetailView


app_name = 'camara'


urlpatterns = [
    
    path(
        'categoria/<slug:slug>/',
        ProductosPorCategoriaListView.as_view(),
        name='productos_categoria'
    ),
    path(
        'producto/<int:pk>/',
        ProductoDetailView.as_view(),
        name='producto_detalle'
    ),
]






