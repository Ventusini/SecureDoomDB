from rest_framework import serializers
from .models import Incident
from .models import Show

class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields=('id', 'date', 'street', 'value')
        read_only_fields = ('id', 'date')     

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields=('id', 'street_name', 'total')
        read_only_fields = ('id', 'date')     