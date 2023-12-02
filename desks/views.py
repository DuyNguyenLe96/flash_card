from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.serializers import CardSerializer
from desks.models import Desk
from desks.serializers import DeskSerializer, DeskCardDetailsSerializer


# Create your views here.

class DeskCardView(APIView):
    def post(self, request):
        deck_serializer = DeskSerializer(data=request.data)
        deck_serializer.is_valid(raise_exception=True)
        deck_serializer.save()
        return Response(deck_serializer.data, status.HTTP_201_CREATED)

    def put(self, request):
        deck_serializer = DeskSerializer(data=request.data)
        deck_serializer.is_valid(raise_exception=True)
        deck_serializer.save()
        if "cards" not in request.data:
            raise ValidationError("missing cards")
        desk = Desk.objects.get(name=deck_serializer.data['name'])
        data_cards = request.data['cards']
        for card in data_cards:
            card["desk"] = desk.id
        print(data_cards)
        cards_serializer = CardSerializer(data=data_cards, many=True)
        cards_serializer.is_valid(raise_exception=True)
        cards_serializer.save()
        result = DeskCardDetailsSerializer(instance=Desk.objects.get(id=1))
        return Response(result.data, status.HTTP_201_CREATED)
