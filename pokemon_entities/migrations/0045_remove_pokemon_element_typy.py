# Generated by Django 3.1.13 on 2021-07-28 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0044_auto_20210728_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='element_typy',
        ),
    ]