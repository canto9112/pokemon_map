# Generated by Django 3.1.13 on 2021-07-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0043_auto_20210728_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='pokemon',
            field=models.ManyToManyField(to='pokemon_entities.Pokemon'),
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='element_typy',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='element_typy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='element_type', to='pokemon_entities.pokemonelementtype'),
        ),
    ]
