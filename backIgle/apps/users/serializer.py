from rest_framework import serializers
from .models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('email', 'name', 'last_name')