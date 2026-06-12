from rest_framework.views import APIView
from rest_framework.response import Response
from services.serializers import ConversaoTemperaturaSerializer
from rest_framework import status 
from rest_framework.parsers import JSONParser

class Conversao(APIView):
    def get(self, request):
        dados = ConversaoTemperaturaSerializer()
        return Response(dados.data)
    def post(self, request):
        try:
            dados_requisicao = JSONParser().parse(request)
            dados = ConversaoTemperaturaSerializer(data=dados_requisicao)
            if dados.is_valid():
                dados.converter()
                return Response(dados.data)
            else:
                return Response(dados.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            contexto = {
                "erro": str(e)
            }

            return Response(contexto, status=status.HTTP_401_UNAUTHORIZED)