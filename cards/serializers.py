from rest_framework import serializers

from cards.models import Card
from desks.models import Desk


class CardSerializer(serializers.ModelSerializer):
    desk = serializers.PrimaryKeyRelatedField(queryset=Desk.objects.all())

    class Meta:
        model = Card
        fields = "__all__"
