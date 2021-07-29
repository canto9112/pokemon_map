# Generated by Django 3.1.13 on 2021-07-27 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0026_auto_20210727_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует'),
        ),
    ]
