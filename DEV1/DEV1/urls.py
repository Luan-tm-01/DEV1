from django.contrib import admin
from django.urls import path, include
from DEV1.views.buscar import BuscarView
from DEV1.views.contato import ContatoView
from .views.estaticas import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('aula/', include("aula.urls", namespace="aula")),
    path('contato/classe/', ContatoView.as_view(), name="contato_classe"),
    path("busca/classe/", BuscarView.as_view(), name="busca"),
]
