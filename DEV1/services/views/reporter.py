from rest_framework import viewsets
from aula.models import Reporter
from services.serializers import ReporterSerializer

class ReporterService(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    lookup_field = "number"