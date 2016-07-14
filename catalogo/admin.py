from django.contrib import admin
from catalogo.models import Categoria, Marca, Producto, Slider



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','banner','orden_clasificacion','estado',
        'created_at','updated_at',)
   

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre','banner','created_at','updated_at',)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','imagen_producto','marca','descripcion',
        'sku','precio','clasificacion','categoria','estado','created_at',
        'updated_at',)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo','imagen','descripcion','orden_clasificacion','estado','created_at','updated_at',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Slider, SliderAdmin)


