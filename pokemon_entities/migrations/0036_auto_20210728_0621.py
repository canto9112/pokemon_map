# Generated by Django 3.1.13 on 2021-07-28 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0035_pokemonelementtype_element_typy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonelementtype',
            old_name='element_typy',
            new_name='pokemon',
        ),
    ]