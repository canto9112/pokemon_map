# Generated by Django 3.1.13 on 2021-07-28 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0031_pokemonelementtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemonelementtype'),
        ),
    ]