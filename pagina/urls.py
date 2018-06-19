from django.urls import path,include
from pagina.views import index,producto_view,producto_list,producto_update,producto_delete,productoList,productoCreate,productoUpdate,productoDelete,ReportePersonasPDF
from django.contrib.auth.decorators import login_required

app_name = 'pagina'

urlpatterns = [
    path('', index,name='index'),
    path('nuevo',productoCreate.as_view(),name='producto_crear'),
    path('listar',productoList.as_view(),name='producto_listar'),
    path('editar/<pk>',productoUpdate.as_view(),name='producto_editar'),
    path('eliminar/<pk>',productoDelete.as_view(),name='producto_eliminar'),
    path('reporte_personas_pdf',ReportePersonasPDF.as_view(), name="reporte_personas_pdf"),
]
