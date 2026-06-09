from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    enderecos = {
        'saudacao_funcao': reverse("services:saudacao_funcao", request=request),
        'saudacao_classe': reverse("services:saudacao_classe", request=request)
    }
    
    return Response(enderecos)