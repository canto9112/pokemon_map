import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from pprint import pprint


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entitys = PokemonEntity.objects.all()

    for pokemon_entity in pokemon_entitys:
        lat = pokemon_entity.lat
        lon = pokemon_entity.lon
        img_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        add_pokemon(folium_map, lat, lon, img_url)

    pokemons_on_page = []

    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemon_id = pokemon.id
        if pokemon.image:
            img_url = request.build_absolute_uri(pokemon.image.url)
        else:
            img_url = pokemon.image
        title = pokemon.title_ru
        pokemons_on_page.append({'pokemon_id': pokemon_id,
                                 'img_url': img_url,
                                 'title_ru': title})

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    requested_pokemon = {}
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon.update({'title_ru': pokemon.title_ru,
                                      'title_en': pokemon.title_en,
                                      'title_jp': pokemon.title_jp,
                                      'description': pokemon.description,
                                      'img_url': request.build_absolute_uri(pokemon.image.url),
                                      'pokemon_id': pokemon.id})
            previous_pokemon = pokemon.previous_evolution
            if previous_pokemon:
                requested_pokemon.update({'previous_evolution': {
                    'title_ru': previous_pokemon.title_ru,
                    'pokemon_id': previous_pokemon.id,
                    'img_url': request.build_absolute_uri(previous_pokemon.image.url)}})

            next_pokemon = pokemon.next_evolution.first()
            if next_pokemon:
                requested_pokemon.update({'next_evolution': {
                    'title_ru': next_pokemon.title_ru,
                    'pokemon_id': next_pokemon.id,
                    'img_url': next_pokemon.image.url
                }})
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entitys = PokemonEntity.objects.filter(pokemon=requested_pokemon['pokemon_id'])
    for pokemon_entity in pokemon_entitys:
        lat = pokemon_entity.lat
        lon = pokemon_entity.lon
        img_url = request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        add_pokemon(folium_map, lat, lon, img_url)

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': requested_pokemon
    })
