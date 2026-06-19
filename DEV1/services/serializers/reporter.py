from rest_framework import serializers
from aula.models import Reporter
from services.mixins import MixinSerializerValidate

class ReporterSerializer(serializers.ModelSerializer, MixinSerializerValidate):

    class Meta:
        model = Reporter
        fields = '__all__'

    