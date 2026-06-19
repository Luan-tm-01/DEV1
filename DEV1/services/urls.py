from django.db import router
from django.urls import path
from services.views import *
from services.views import Calculo, Conversao, Frete
from rest_framework.routers import DefaultRouter
from services.views import ReporterService, PassaporteServiceList, PassaporteService
from rest_framework.authtoken.views import obtain_auth_token

app_name = "services"

routers = DefaultRouter()

router.register('reporters', ReporterService, 'reporter')

urlpatterns = [
   path("", api_root, name="api_root"),
   path('saudacao', saudacao, name="saudacao_funcao"),
   path('saudacao_classe', Saudacao.as_view(), name="saudacao_classe"),
   path('calcular', Calculo.as_view(), name="calcular"),
   path('conversao', Conversao.as_view(), name ="conversao"),
   path('frete', Frete.as_view(), name ="frete"),
   path('pessoa', PessoaSimplesService.as_view(), name="pessoa_simples"),
   path('pessoa/<int:pk>', PessoaService.as_view(), name="pessoa_object"),
   path("passaporte", PassaporteServiceList.as_view(), name="passaporte_listar_criar"),
   path("passaporte/<int:pk>", PassaporteService.as_view(), name="passaporte"),
   path("autenticar", obtain_auth_token),
]

urlpatterns += router.urls