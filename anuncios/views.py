from rest_framework import generics

from . models import Anuncio
from . serializers import AnuncioSerializer


class AnunciosListAPI(generics.ListAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class AnunciosDetailsAPI(generics.RetrieveDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
