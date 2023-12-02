# Generated by Django 4.2.7 on 2023-12-02 06:16

import cards.models
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_image', models.ImageField(blank=True, null=True, upload_to=functools.partial(cards.models.wrapper_front, *(), **{'target': 'front'}))),
                ('front_text', models.TextField(help_text='Text of the front card', verbose_name='Front Text Card')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to=functools.partial(cards.models.wrapper_back, *(), **{'target': 'back'}))),
                ('back_text', models.TextField(help_text='Text of the behind card', verbose_name='Back Text Card')),
                ('desk', models.ForeignKey(help_text='Desk contain the flash cards', on_delete=django.db.models.deletion.CASCADE, related_name='card_desk', to='desks.desk', verbose_name='Desk cards')),
            ],
            options={
                'db_table': 'cards',
            },
        ),
    ]
