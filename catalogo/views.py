from django.shortcuts import render, get_object_or_404
from catalogo.models import Categoria, Marca, Producto, Slider
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def view_index(request):
    sliders = Slider.objects.filter(estado='true')
    sliders.order_by('orden_clasificacion')
    categorias = Categoria.objects.filter(estado='true')
       
    return render(request, 'home.html', {'sliders':sliders, 'categorias':categorias})




def categoria(request, pk):
    categorias = Categoria.objects.filter(estado='true')
    categoria = get_object_or_404(Categoria, pk=pk)
    producto = Producto.objects.filter(categoria__id=categoria.pk)
    paginator = Paginator(producto, 6)
    page = request.GET.get('page')
    
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        productos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        productos = paginator.page(paginator.num_pages)

    
    return render(request, 'categoria.html', {'categorias':categorias, 'categoria':categoria, 'producto':producto, 'productos':productos})

def detalle_producto(request, pk):
    categorias = Categoria.objects.filter(estado='true')
    producto = get_object_or_404(Producto, pk=pk)
    
    return render(request, 'producto.html', {'categorias': categorias, 'producto':producto})


