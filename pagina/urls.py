from django.urls import path,include
from pagina.views import index,producto_view,producto_list,producto_update,producto_delete

app_name = 'pagina'

urlpatterns = [
    path('', index,name='index'),
    path('nuevo',producto_view,name='producto_crear'),
    path('listar',producto_list,name='producto_listar'),
    path('editar/<idProducto>',producto_update,name='producto_editar'),
    path('eliminar/<idProducto>',producto_delete,name='producto_eliminar'),

]
