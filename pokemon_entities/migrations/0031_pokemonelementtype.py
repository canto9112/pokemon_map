# Generated by Django 3.1.13 on 2021-07-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0030_auto_20210727_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('element_typy', models.ManyToManyField(to='pokemon_entities.Pokemon')),
            ],
        ),
    ]