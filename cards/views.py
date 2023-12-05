from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.serializers import CardSerializer


# Create your views here.
class CardView(APIView):

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
