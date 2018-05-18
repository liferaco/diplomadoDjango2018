from django.urls import path,include
from pagina.views import index

urlpatterns = [
    path('', index),
]
