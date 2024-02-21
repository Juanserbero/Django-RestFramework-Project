from rest_framework import serializers
from.models import*

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = "__all__"