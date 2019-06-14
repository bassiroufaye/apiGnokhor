from rest_framework import serializers
#from todos import models
from apiGnokhor import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nom',
            'prenom',
            'adresse',
            'telephone',
            'image',
        )
        model = models.Client

class LunetteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nom',
            'typelunette',
            'prix',
            'photo',
        )
        model = models.Lunette