from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ClasesSerializer
from apps.users.authorization_mixin import Authentication

class ClasesVieset(Authentication, ModelViewSet):
    serializer_class=ClasesSerializer
    queryset = ClasesSerializer.Meta.model.objects.all()