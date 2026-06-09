from django.urls import path
from services.views import *

app_name = "services"

urlpatterns = [
   path("", api_root, name="api_root"),
   path('saudacao', saudacao, name="saudacao_funcao"),
   path('saudacao_classe', Saudacao.as_view(), name="saudacao_classe")
   
]