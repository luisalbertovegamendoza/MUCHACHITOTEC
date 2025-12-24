from django.urls import path
from .views import ProductosPorCategoriaListView, ProductoDetailView
from .views import HomeView



urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),

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






