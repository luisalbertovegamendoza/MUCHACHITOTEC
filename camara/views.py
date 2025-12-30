from django.shortcuts import render


from django.views.generic import (DetailView,ListView , CreateView , UpdateView , DeleteView)
from django.shortcuts import get_object_or_404
from .models import Producto, Category



    
class ProductosPorCategoriaListView(ListView):
    model = Producto
    template_name = 'camara/listar_categoria.html'
    context_object_name = 'productos'

    def get_queryset(self):
        self.categoria = get_object_or_404(
            Category,
            slug=self.kwargs['slug']
        )


        # ✅ GUARDAR LA CATEGORÍA EN SESSION
        self.request.session['ultima_categoria'] = self.categoria.slug


        return Producto.objects.filter(
            category=self.categoria,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context
    
    
    

class ProductoDetailView(DetailView):
    model=Producto  # Modelo que usará
    template_name='camara/producto_detalle.html' # Plantilla a renderizar
    context_object_name='producto' #  Nombre de la variable en la plantilla

