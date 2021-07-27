from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_jp = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(upload_to='image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.ForeignKey, blank=True, null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)

    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.pokemon)
