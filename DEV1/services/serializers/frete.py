
from rest_framework import serializers
from services.serializers.enumerations import FreteRegiao

class FreteSerializer(serializers.Serializer):

    peso = serializers.FloatField(required=True)
    regiao_origem = serializers.ChoiceField(required=True, choices=FreteRegiao)
    regiao_destino = serializers.ChoiceField(required=True, choices=FreteRegiao)
    valor_base = serializers.FloatField(required=False)
    adicional_peso = serializers.FloatField(required=False)
    adicional_regiao = serializers.FloatField(required=False)
    valor_total = serializers.FloatField(required=False)

    class Meta:
        fields = ['peso', 'regiao_origem', 'regiao_destino']

    def calcular_frete(self):
        peso = self.validated_data.get("peso")
        regiao_origem = self.validated_data.get("regiao_origem")
        regiao_destino = self.validated_data.get("regiao_destino")

        if peso < 5: adicional_peso += 5.00
        elif peso >= 5 and peso < 10: adicional_peso += 10.00
        elif peso >= 10 and peso < 15: adicional_peso += 15.00
        elif peso >= 15: adicional_peso += (20.00) * peso//15

        if regiao_origem == regiao_destino: adicional_regiao += 10.00
        elif regiao_origem == FreteRegiao.SUL and FreteRegiao.SUDESTE or regiao_origem == FreteRegiao.SUDESTE and FreteRegiao.SUL: 
            adicional_regiao += 20.00
        elif regiao_origem == FreteRegiao.NORTE and FreteRegiao.NORDESTE or regiao_origem == FreteRegiao.NORDESTE and FreteRegiao.NORTE: 
            adicional_regiao += 25.00
        elif regiao_origem == FreteRegiao.CENTRO_OESTE and FreteRegiao.SUDESTE or regiao_origem == FreteRegiao.SUDESTE and FreteRegiao.CENTRO_OESTE: 
            adicional_regiao += 20.00
        else:
            adicional_regiao += 50.00