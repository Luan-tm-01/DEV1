from django.forms import ValidationError
from rest_framework import serializers
from aula.models import Pessoa

class PessoaMinimoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pessoa
        fields = ["id", "nome"]

class PessoaCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = '__all__' #verificar

    def validate(self, attrs):
        pessoa = self.instance
        try:
            pessoa.full_clean()
        except ValidationError as erros:
            raise serializers.ValidationError(erros.message_dict)
        
        return attrs