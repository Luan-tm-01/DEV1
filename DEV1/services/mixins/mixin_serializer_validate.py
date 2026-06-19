from django.forms import ValidationError
from rest_framework import serializers

class MixinSerializerValidate:
    def validate(self, attrs):
            obj = self.instance
            try:
                obj.full_clean()
            except ValidationError as erros:
                raise serializers.ValidationError(erros.message_dict)
            
            return attrs