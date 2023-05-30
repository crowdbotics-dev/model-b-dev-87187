from rest_framework import authentication
from test_app.models import ModelA
from .serializers import ModelASerializer
from rest_framework import viewsets

class ModelAViewSet(viewsets.ModelViewSet):
    serializer_class = ModelASerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = ModelA.objects.all()