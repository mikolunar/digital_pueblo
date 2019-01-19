from rest_framework import serializers
from . models import Anuncio


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Anuncio
