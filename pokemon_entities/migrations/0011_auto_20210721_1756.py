# Generated by Django 3.1.13 on 2021-07-21 17:56

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20210721_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(default=1, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
            preserve_default=False,
        ),
    ]
