# Generated by Django 3.1.13 on 2021-07-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0042_auto_20210728_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_typy',
            field=models.ManyToManyField(blank=True, null=True, to='pokemon_entities.PokemonElementType'),
        ),
    ]