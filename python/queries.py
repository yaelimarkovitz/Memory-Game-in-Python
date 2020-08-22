from connenctions import insert_data, query_data
#exercise 1
def heavy_pokemon():
    return(query_data("SELECT name, MAX(weight) FROM pokemon"))

#exercise 2
def find_by_type(type):
    return(query_data("SELECT name FROM pokemon WHERE type = \"" + type + "\""))

#exercise 3
def find_owners(name):
    return(query_data("SELECT id_trainer FROM pokemon , trainer_of_pokemon WHERE id_pokemon = pokemon.id and name = \"" + name +"\""))

def find_roster(trainer):
    return(query_data("SELECT pokemon.name FROM pokemon , trainer , trainer_of_pokemon WHERE id_pokemon = pokemon.id and id_trainer = trainer.name and trainer.name = \"" + trainer +"\""))

print(heavy_pokemon())
print(find_by_type("grass"))
print(find_owners("gengar"))
print(find_roster("Loga"))

