from .connenctions import insert_data, query_data
from .trainer_modul import insert_trainer, insert_trainer_of_pokemon
from .types_modul import insert_type, insert_type_of_pokemon

def insert_pokemon(pokemon):
    if pokemon["id"] in list(map(lambda param: param["id"] ,query_data("SELECT id FROM pokemon"))):
        raise KeyError("this pokemon already exists")
    values = "( {}, \"{}\", {}, {},\"{}\")".format(str(pokemon["id"]) ,pokemon["name"] , str(pokemon["height"]),str(pokemon["weight"]),
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png".format(str(pokemon["id"] )) )
    insert_data("pokemon",values)

    if "ownedBy" in pokemon:
        for trainer in pokemon["ownedBy"]:
            insert_trainer(trainer)
            insert_trainer_of_pokemon(trainer["name"],pokemon["id"])
    if(isinstance(pokemon["type"],list)):
        for type_ in pokemon["type"]:
            insert_type(type_)
            insert_type_of_pokemon(type_,pokemon["id"])
    else:
        insert_type(pokemon["type"])
        insert_type_of_pokemon(pokemon["type"],pokemon["id"])

def insert_pokemons(json_data):
    for pokemon in json_data:
        insert_pokemon(pokemon)

#exercise 1
def heavy_pokemon():
    return list(map(lambda param:param["name"],
    (query_data("SELECT name FROM pokemon WHERE pokemon.weight >= ALL (select weight from pokemon)"))))

#exercise 2
def find_by_type(type):
    return list(map(lambda param:param["name"],
    (query_data("SELECT pokemon.name FROM type_pokemon, pokemon WHERE pokemon.id = type_pokemon.pokemon_id and type_id = \"" + type + "\""))))

def add_type(type_name,pokemon):
    insert_data("types", ''' ( "{}" )'''.format(type_name))
    insert_data("type_pokemon",'''( "{}",{})'''.format(type_name,pokemon))

#exercise 3
def find_owners(name):
    return list(map(lambda param: param["id_trainer"],
    (query_data("SELECT DISTINCT id_trainer FROM pokemon , trainer_of_pokemon \
                WHERE id_pokemon = pokemon.id and name = \"" + name +"\""))))

def find_roster(trainer):
    return list(map(lambda name: name["name"],
    (query_data("SELECT DISTINCT pokemon.name FROM pokemon , trainer , trainer_of_pokemon \
                WHERE id_pokemon = pokemon.id and id_trainer = trainer.name and trainer.name = \"" + trainer +"\""))))

def most_owned():
    return list(map(lambda param: param["id_pokemon"],
    (query_data("SELECT id_pokemon FROM trainer_of_pokemon \
                GROUP BY id_pokemon HAVING count(*) >= ALL\
                (SELECT COUNT(*) FROM trainer_of_pokemon GROUP BY id_pokemon)"))))

def delete_pokemon(pokemon_id, trainer_id):
    query_data("DELETE FROM trainer_of_pokemon\
                WHERE id_pokemon = {} and id_trainer = \"{}\"".format(pokemon_id,trainer_id))
    
def get_url(pokemon_id):
    return list(map(lambda param: param["picture"],query_data("SELECT picture FROM pokemon WHERE id = {}".format(str(pokemon_id)))))



print(heavy_pokemon())
print(find_by_type("grass"))
# print(find_owners("gengar"))
# print(find_roster("Loga"))
# print(most_owned())

