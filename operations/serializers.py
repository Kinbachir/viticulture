from rest_framework import serializers
from .models import Exploitation, Salarie, OperationCulturale, OperationPhytosanitaire

class ExploitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exploitation
        fields = '__all__'

class SalarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salarie
        fields = '__all__'

class OperationCulturaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationCulturale
        fields = '__all__'

class OperationPhytosanitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationPhytosanitaire
        fields = '__all__'
