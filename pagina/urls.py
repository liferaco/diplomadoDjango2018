from django.urls import path,include
from pagina.views import index,producto_view

app_name = 'pagina'

urlpatterns = [
    path('', index,name='index'),
    path('nuevo', producto_view,name='producto_crear'),
]
