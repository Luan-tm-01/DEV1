from rest_framework import serializers
from services.serializers.enumerations import Operacao

class CalculoSerializer(serializers.Serializer):

    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required=True, choices=Operacao)
    resultado = serializers.CharField(required=False)

    class Meta:
        fields = ['primeiro_termo', 'segundo_termo', 'operacao']

    def calcular(self):
        primeiro_valor = self.validated_data.get("primeiro_termo")
        segundo_valor = self.validated_data.get("segundo_termo")
        op = self.validated_data.get("operacao")

        match op:
            case Operacao.ADICAO:
                self.validated_data.update({"resultado": primeiro_valor + segundo_valor})
                self.validated_data.update({"operacao": Operacao.ADICAO.label})
            case Operacao.SUBTRACAO:
                resultado = primeiro_valor - segundo_valor
                self.validated_data.update(resultado)
                self.validated_data.update({"operacao": Operacao.SUBTRACAO})
            case Operacao.MULTIPLICAÇÃO:
                resultado = primeiro_valor * segundo_valor
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operacao": Operacao.MULTIPLICAÇÃO})
            case Operacao.DIVISAO:
                resultado = primeiro_valor / segundo_valor
                self.validated_data.update({"resultado": resultado})
                self.validated_data.update({"operacao": Operacao.DIVISAO})
            case _:
                raise NotImplementedError("Operação não Implementada")
            