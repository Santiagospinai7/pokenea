from rest_framework import serializers
from .models import Pokenea

class PokeneaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokenea
        fields = '__all__'