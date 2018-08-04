from rest_framework import serializers
from .models import Incident
from .models import Show

class IncidentsSerializer(serializers.ModelSerializer):
    street_name = serializers.StringRelatedField(source='street', read_only=True)
    class Meta:
        model = Incident
        fields=('id', 'date', 'street_name')
        read_only_fields = ('id', 'date')     

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields=('id', 'street', 'total')
        read_only_fields = ('id', 'date')     