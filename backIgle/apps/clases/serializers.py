from rest_framework import serializers
from .models import Clases

class ClasesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clases
        fields = '__all__'