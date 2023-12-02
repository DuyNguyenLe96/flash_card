import os
from functools import partial

from django.core.exceptions import ValidationError
from django.db import models

from desks.models import Desk


def wrapper_front(instance, filename, target):
    ext = filename.split(".")[-1].lower()
    if ext not in ["jpg", "png", "jpeg"]:
        raise ValidationError(f"invalid image extension: {filename}")
    filename = f"{instance.front_text.replace(' ', '_')}.{ext}"
    return os.path.join(target, filename)


def wrapper_back(instance, filename, target):
    ext = filename.split(".")[-1].lower()
    if ext not in ["jpg", "png", "jpeg"]:
        raise ValidationError(f"invalid image extension: {filename}")
    filename = f"{instance.front_text.replace(' ', '_')}.{ext}"
    return os.path.join(target, filename)


# Create your models here.
class Card(models.Model):
    front_image = models.ImageField(upload_to=partial(wrapper_front, target="front"), null=True, blank=True)
    front_text = models.TextField(verbose_name="Front Text Card", help_text="Text of the front card")
    back_image = models.ImageField(upload_to=partial(wrapper_back, target="back"), null=True, blank=True)
    back_text = models.TextField(verbose_name="Back Text Card", help_text="Text of the behind card")
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE, related_name="card_desk", verbose_name="Desk cards",
                             help_text="Desk contain the flash cards")

    class Meta:
        db_table = "cards"
