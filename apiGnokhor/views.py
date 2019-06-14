from django.shortcuts import render

# api/views.py
from rest_framework import generics

#from todos import models
from apiGnokhor import models
from . import serializers

class ListClient(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class ListLunette(generics.ListCreateAPIView):
    queryset = models.Lunette.objects.all()
    serializer_class = serializers.LunetteSerializer

class DetailLunette(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lunette.objects.all()
    serializer_class = serializers.LunetteSerializer

# Create your views here.
