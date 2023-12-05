# Generated by Django 4.2.7 on 2023-12-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_is_front'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='is_front',
            field=models.BooleanField(default=True, help_text='Card front side set True and card back side set False', verbose_name='Front Side'),
        ),
    ]