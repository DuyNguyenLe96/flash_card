from django.urls import path, include

from .views import DeskCardView

urlpatterns = [
    path("desk/", include([
        path("cards", DeskCardView.as_view(), name="desk_cards")
    ]))
]
