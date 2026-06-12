
from rest_framework import serializers
from services.serializers.enumerations import Temperatura

class ConversaoTemperaturaSerializer(serializers.Serializer):

    temperatura_origem = serializers.ChoiceField(required=True, choices=Temperatura)
    temperatura_convertida = serializers.ChoiceField(required=True, choices=Temperatura)
    valor_inicial = serializers.FloatField(required=True)
    valor_convertido = serializers.FloatField(required=False)

    class Meta:
        fields = ['temperatura_origem', 'temperatura_convertida', 'valor_inicial']

    def converter(self):
        temperatura_origem = self.validated_data.get("temperatura_origem")
        temperatura_convertida = self.validated_data.get("temperatura_convertida")
        valor_inicial = self.validated_data.get("valor_inicial")
        op = self.validated_data.get("conversao")

        if temperatura_origem == Temperatura.CELSIUS and temperatura_convertida == Temperatura.FAHRENHEIT:
            valor_convertido = (valor_inicial*1.8) + 32
            self.validated_data.update({"valor_convertido": valor_convertido})

        elif temperatura_origem == Temperatura.FAHRENHEIT and temperatura_convertida == Temperatura.CELSIUS:
            valor_convertido = ((valor_inicial-32) * 5) / 9
            self.validated_data.update({"valor_convertido": valor_convertido})

        elif temperatura_origem == Temperatura.CELSIUS and temperatura_convertida == Temperatura.KELVIN:
            valor_convertido = valor_inicial + 273.15
            self.validated_data.update({"valor_convertido": valor_convertido})

        elif temperatura_origem == Temperatura.KELVIN and temperatura_convertida == Temperatura.CELSIUS:
            valor_convertido = valor_inicial - 273.15
            self.validated_data.update({"valor_convertido": valor_convertido})

        elif temperatura_origem == Temperatura.FAHRENHEIT and temperatura_convertida == Temperatura.KELVIN:
            valor_convertido = (((valor_inicial-32) * 5) / 9) + 273.15
            self.validated_data.update({"valor_convertido": valor_convertido})

        elif temperatura_origem == Temperatura.KELVIN and temperatura_convertida == Temperatura.FAHRENHEIT:
            valor_convertido = ((valor_inicial-273.15) * 1.8) + 32
            self.validated_data.update({"valor_convertido": valor_convertido})


        else:
            raise NotImplementedError("Operação não Implementada")