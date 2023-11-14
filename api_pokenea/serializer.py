from rest_framework import serializers
# from .models import Pokenea
from pages.models import Pokenea

class PokeneaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokenea
        fields = ['id', 'name', 'height', 'skill']