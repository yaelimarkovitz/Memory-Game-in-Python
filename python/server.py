from flask import Flask, request,Response
from pokemons_modul import find_roster , find_owners , add_type , find_by_type,insert_pokemon,delete_pokemon,get_url
import requests
import json

app = Flask(__name__)
port_number = 3000

@app.route('/sanity')
def index():
    return("server up and running")

@app.route('/trainers/<trainer_name>')
def pokemons_of_triner(trainer_name):
    return json.dumps({"pokemons":find_roster(trainer_name)}),200

@app.route('/pokemons/<pokemon>')
def owners_of_pokemon(pokemon):
    return json.dumps({"owners": find_owners(pokemon)}),200

@app.route('/pokemons/' , methods = ['POST'])
def add_pokemon():
    try:
        data = request.get_json()
        insert_pokemon(data)
        return json.dumps({"created":data}),201
    except KeyError as exp:
        return json.dumps({"error":exp.args}) , 409

@app.route('/pokemons/', methods = ['PUT'])
def update_type():
    pokemon = request.get_json()
    url_poke_api = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon["id"]),verify=False).json()
    pokemon_types = url_poke_api["types"]
    for type in pokemon_types:
        add_type(type["type"]["name"],pokemon["id"])
    return json.dumps({"updated":[param["type"]["name"] for param in pokemon_types]}),200



@app.route('/type/<type_name>')
def get_by_type(type_name):
    return json.dumps({"names":find_by_type(type_name)}),200


@app.route('/pokemons', methods = ['PATCH'])
def delete_poke():
    data_to_del = request.get_json()
    delete_pokemon(data_to_del["pokemon_id"],data_to_del["trainer_id"])
    return json.dumps({"deleted": data_to_del}),200

@app.route('/pictures/<pokemon_id>')
def get_picture(pokemon_id):
    return json.dumps({"picture_url":get_url(pokemon_id)})


app.run(port=port_number)