
from .connenctions import insert_data, query_data

def insert_type(type):
    types = []
    types_dict = query_data("SELECT * FROM types")
    for t in types_dict:
        types.append(t["name"])
    if type not in types:
        values = ''' ( "{}")'''.format(type)
        insert_data("types",values)

def insert_type_of_pokemon(type,pokemon_id):
    values = ''' ( "{}" , {}) '''.format(type,pokemon_id)
    insert_data("type_pokemon" , values)