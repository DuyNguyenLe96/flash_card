from django.urls import path

from cards.views import CardView

urlpatterns = [
    path("cards", CardView.as_view(), name="create_cards")

]
