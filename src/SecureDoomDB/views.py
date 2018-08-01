from django.shortcuts import render
from rest_framework import generics
from .serializers import IncidentsSerializer
from .models import Incident
from django.db.models import Sum
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.values('street__name').annotate(Sum('value'))
    serializer_class=IncidentsSerializer

    def perform_create(self,serializer):
        serializer.save()

