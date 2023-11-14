from rest_framework import viewsets
from .serializer import PokeneaSerializer
from pages.models import Pokenea


class PokeneaViewSet(viewsets.ModelViewSet):
   queryset = Pokenea.objects.all()
   serializer_class = PokeneaSerializer
