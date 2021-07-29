from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200,
                                verbose_name='Русское имя')

    title_en = models.CharField(max_length=200,
                                verbose_name='Английское имя',
                                blank=True)

    title_jp = models.CharField(max_length=200,
                                verbose_name='Японское имя',
                                blank=True)

    image = models.ImageField(upload_to='image/',
                              verbose_name='Изображение',
                              null=True)

    description = models.TextField(verbose_name='Описание',
                                   blank=True)

    previous_evolution = models.ForeignKey('Pokemon',
                                           verbose_name='Из кого эволюционирует',
                                           related_name='next_evolution',
                                           on_delete=models.SET_NULL,
                                           blank=True,
                                           null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')

    lat = models.FloatField(verbose_name='Долгота')
    lon = models.FloatField(verbose_name='Широта')

    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время исчезновения')

    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Атака')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return str(self.pokemon)
