from django.contrib import admin
from django.urls import path, include
from .views.estaticas import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('aula/', include("aula.urls", namespace="aula")),
]
