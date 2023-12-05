from django.db.models import Q

from cards.models import Card
from cards.serializers import BackCardSerializer, FrontCardSerializer


def slip_card_front_or_back(params):
    def _str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    print(params)
    filters = Q(id=int(params.get("id")))
    card = Card.objects.filter(filters)[0]
    if "is_front" in params:
        is_front = _str2bool(params.get("is_front"))
        print(is_front)
        if is_front:
            back = {"back_text": card.back_text, "back_image": card.back_image}
            result = BackCardSerializer(instance=back)
        else:
            front = {"front_text": card.front_text, "front_image": card.front_image}
            result = FrontCardSerializer(instance=front)
    return result.data
