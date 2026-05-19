from django.contrib import admin
from django.urls import path, include
from DEV1.views.buscar import BuscarView
from DEV1.views.contato import ContatoView
from DEV1.views.perfil import PerfilView
from .views.estaticas import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('aula/', include("aula.urls", namespace="aula")),
    path('contato/classe/', ContatoView.as_view(), name="contato_classe"),
    path("busca/classe/", BuscarView.as_view(), name="busca"),
    path("contas/login/", auth_views.LoginView.as_view(template_name="contas/login.html", authentication_form="" )),
    path("contas/", include('django.contrib.auth.urls')),
    path("contas/perfil", PerfilView.as_view(), name="perfil")
]
