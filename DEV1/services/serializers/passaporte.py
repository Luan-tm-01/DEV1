from rest_framework import serializers
from aula.models import Passaporte

class PassaporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passaporte
        fields = '__all__'

        