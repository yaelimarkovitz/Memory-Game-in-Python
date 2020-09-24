import json
from .pokemons_modul import insert_pokemons


def load_data(path):
    data = {}
    with open (path,"r") as json_file:
        data = json.load(json_file)
    insert_pokemons(data)

load_data("python/poke_data.json")

