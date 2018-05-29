from django.urls import path,include
from pagina.views import index,producto_view,producto_list

app_name = 'pagina'

urlpatterns = [
    path('', index,name='index'),
    path('nuevo', producto_view,name='producto_crear'),
    path('listar', producto_list,name='producto_listar'),
]
