from django.shortcuts import render


from django.views.generic import (DetailView,ListView , CreateView , UpdateView , DeleteView)
from django.shortcuts import get_object_or_404
from .models import Producto, Category
from django.db.models import Q




    
class ProductosPorCategoriaListView(ListView):
    model = Producto
    template_name = 'camara/listar_categoria.html'
    context_object_name = 'productos'

    def get_queryset(self):
        self.categoria = get_object_or_404(
            Category,
            slug=self.kwargs['slug']
        )

        self.request.session['ultima_categoria'] = self.categoria.slug


        queryset = Producto.objects.filter(category=self.categoria)

#BUSQUEDA POR PALABRAS
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(nombre__icontains=q) |
                Q(detalle__icontains=q)
            )

          # -------- FILTRO PRECIO --------
        min_price = self.request.GET.get('min')
        max_price = self.request.GET.get('max')

        if min_price:
            queryset = queryset.filter(precio__gte=min_price)

        if max_price:
            queryset = queryset.filter(precio__lte=max_price)

        # -------- FILTRO STOCK --------
        stock = self.request.GET.get('stock')
        if stock == 'disponible':
            queryset = queryset.filter(stock__gt=0, disponible=True)

        # -------- ORDEN --------
        orden = self.request.GET.get('orden')
        if orden == 'precio_asc':
            queryset = queryset.order_by('precio')
        elif orden == 'precio_desc':
            queryset = queryset.order_by('-precio')
        elif orden == 'nombre':
            queryset = queryset.order_by('nombre')

        return queryset






    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context
    
    
    

class ProductoDetailView(DetailView):
    model=Producto  # Modelo que usará
    template_name='camara/producto_detalle.html' # Plantilla a renderizar
    context_object_name='producto' #  Nombre de la variable en la plantilla

