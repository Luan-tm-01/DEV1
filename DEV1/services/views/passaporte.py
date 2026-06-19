from rest_framework.generics import ListCreateAPIView
from services.serializers.passaporte import PassaporteSerializer
from aula.models import Passaporte
from rest_framework import generics

class PassaporteServiceList(ListCreateAPIView):
    queryset = Passaporte.objects.all()
    serializer_class = PassaporteSerializer

class PassaporteService(UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Passaporte.objects.all()
    serializer_class = PassaporteSerializer 