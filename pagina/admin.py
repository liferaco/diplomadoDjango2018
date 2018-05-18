from django.contrib import admin
from .models import marca
from .models import producto
from .models import movimiento
from .models import stock

# Register your models here.
class marcaAdmin(admin.ModelAdmin):
	list_display=('id','nombre')

class productoAdmin(admin.ModelAdmin):
	list_display=('id','idMarca_id','codigo','nombre','tipo','costo')

class stockAdmin(admin.ModelAdmin):
	list_display=('id','idProducto_id','total',)

class movimientoAdmin(admin.ModelAdmin):
	list_display=('id','idProducto_id','fecha','nomMovimiento','cantidad')

admin.site.register(marca,marcaAdmin)
admin.site.register(producto,productoAdmin)
admin.site.register(movimiento,movimientoAdmin)
admin.site.register(stock,stockAdmin)

