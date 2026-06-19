from django.shortcuts import get_object_or_404
from rest_framework.views import APIView,Response
from rest_framework import status
from services.views import BaseSecurity
from aula.models import Pessoa
from services.serializers import PessoaMinimoSerializer, PessoaCompleteSerializer

class PessoaSimplesService(BaseSecurity, APIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaMinimoSerializer 

    #Fazer o formato tbm
    def get(self, request):
        pessoa = Pessoa.objects.all()
        contexto = {
            'request': request
        }

        serializador = PessoaMinimoSerializer(pessoa, many=True, context=contexto)

        return Response(serializador.data)
    
class PessoaService(BaseSecurity, APIView):
    serializer_class = PessoaCompleteSerializer
    query_set = Pessoa.objects.all()

    def get(self, request, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        contexto = {
            "request": request
        }

        serializador = PessoaCompleteSerializer(pessoa, context=contexto)

        return Response(serializador.data)
    
    def delete(self, request, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa_dados = request.data
        contexto = {
            "request": request
        }

        serializador = PessoaCompleteSerializer(pessoa, data=pessoa_dados, context=contexto)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)