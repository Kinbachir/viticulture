from rest_framework import viewsets
from .models import Exploitation, Salarie, OperationCulturale, OperationPhytosanitaire
from .serializers import (
    ExploitationSerializer,
    SalarieSerializer,
    OperationCulturaleSerializer,
    OperationPhytosanitaireSerializer
)

class ExploitationViewSet(viewsets.ModelViewSet):
    queryset = Exploitation.objects.all()
    serializer_class = ExploitationSerializer

class SalarieViewSet(viewsets.ModelViewSet):
    queryset = Salarie.objects.all()
    serializer_class = SalarieSerializer

class OperationCulturaleViewSet(viewsets.ModelViewSet):
    queryset = OperationCulturale.objects.all()
    serializer_class = OperationCulturaleSerializer

class OperationPhytosanitaireViewSet(viewsets.ModelViewSet):
    queryset = OperationPhytosanitaire.objects.all()
    serializer_class = OperationPhytosanitaireSerializer
