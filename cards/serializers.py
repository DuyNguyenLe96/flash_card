from rest_framework import serializers

from cards.models import Card
from desks.models import Desk


class CardSerializer(serializers.ModelSerializer):
    desk = serializers.PrimaryKeyRelatedField(queryset=Desk.objects.all(), required=False)

    class Meta:
        model = Card
        fields = "__all__"


class FrontCardSerializer(serializers.Serializer):
    front_text = serializers.CharField()
    front_image = serializers.CharField()


class BackCardSerializer(serializers.Serializer):
    back_text = serializers.CharField()
    back_image = serializers.CharField()
