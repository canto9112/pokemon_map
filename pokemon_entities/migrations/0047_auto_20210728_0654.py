# Generated by Django 3.1.13 on 2021-07-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0046_pokemon_element_typy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_typy',
            field=models.ManyToManyField(blank=True, null=True, related_name='next_evolution', to='pokemon_entities.PokemonElementType'),
        ),
    ]