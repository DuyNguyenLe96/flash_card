from rest_framework import serializers

from cards.serializers import CardSerializer
from .models import Desk


class DeskCardDetailsSerializer(serializers.ModelSerializer):
    card_desk = CardSerializer(many=True)

    class Meta:
        model = Desk
        fields = "__all__"


class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desk
        fields = "__all__"
