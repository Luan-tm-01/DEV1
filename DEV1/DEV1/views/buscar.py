from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from aula.models import Pessoa, Aluno
from django.db.models import Q

class BuscarView(View):
    @staticmethod
    def get(request):
        resultados = {}
        query = request.GET.get("query")
        
        pessoas = Pessoa.objects.filter(Q(nome__icontains=query) | 
                                        Q(cpf__icontains=query))
        
        #datas
        #Q(data_nascimento__year=query) | 
        #Q(data_nascimento__month=query) | 
        #Q(data_nascimento__day=query)
        
        pessoas_urls = []
        for pessoa in pessoas:
            url = reverse_lazy("aula:funcao_pessoa_ler", kwargs={"id": pessoa.id})

            pessoas_urls.append((url, pessoa))

        if len(pessoas_urls) > 0:
            resultados['Pessoa'] = pessoas_urls
        else: 
            resultados = None

        contexto = {
            "resultados": resultados,
            "query": query,
        }

        return render(request, "buscar/resultado.html", contexto)