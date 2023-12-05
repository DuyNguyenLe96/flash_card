import os
from functools import partial

from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def wrapper(instance, filename, target):
    ext = filename.split(".")[-1]
    if ext not in ["jpg", "png", "jpeg"]:
        raise ValidationError(f"invalid image extension: {filename}")
    filename = f"{instance.name.replace(' ', '_')}.{ext}"
    return os.path.join(target, filename)


class Desk(models.Model):
    image = models.ImageField(upload_to=partial(wrapper, target="desk"), null=True, blank=True,
                              verbose_name="Image desk",
                              help_text="Image for desk")
    name = models.CharField(max_length=100, unique=True, verbose_name="Name desk",
                            help_text="Name of desk")
    description = models.TextField(null=True, verbose_name="Desk Description",
                                   help_text="Describe information about desk")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "desks"
