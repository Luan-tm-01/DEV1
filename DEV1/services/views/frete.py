from rest_framework.views import APIView
from rest_framework.response import Response
from services.serializers import FreteSerializer
from rest_framework import status 
from rest_framework.parsers import JSONParser

class Frete(APIView):
    def get(self, request):
        dados = FreteSerializer()
        return Response(dados.data)
    def post(self, request):
        try:
            dados_requisicao = JSONParser().parse(request)
            dados = FreteSerializer(data=dados_requisicao)
            if dados.is_valid():
                dados.calcular_frete()
                return Response(dados.data)
            else:
                return Response(dados.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            contexto = {
                "erro": str(e)
            }

            return Response(contexto, status=status.HTTP_401_UNAUTHORIZED)