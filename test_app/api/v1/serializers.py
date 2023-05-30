from rest_framework import serializers
from test_app.models import ModelA

class ModelASerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelA
        fields = "__all__"