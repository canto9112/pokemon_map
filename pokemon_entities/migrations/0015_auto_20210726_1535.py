# Generated by Django 3.1.13 on 2021-07-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_pokemon_show_pokemon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='show_pokemon',
            new_name='description',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='english_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='japan_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
