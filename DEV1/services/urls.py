from django.urls import path
from services.views import *
from services.views import Calculo, Conversao, Frete

app_name = "services"

urlpatterns = [
   path("", api_root, name="api_root"),
   path('saudacao', saudacao, name="saudacao_funcao"),
   path('saudacao_classe', Saudacao.as_view(), name="saudacao_classe"),
   path('calcular', Calculo.as_view(), name="calcular"),
   path('conversao', Conversao.as_view(), name ="conversao"),
   path('frete', Frete.as_view(), name ="frete"),
   path('pessoa', PessoaSimplesService.as_view(), name="pessoa_simples"),
   path('pessoa/<int:pk>', PessoaService.as_view(), name="pessoa_object")
   
]