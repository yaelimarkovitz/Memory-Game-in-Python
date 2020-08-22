import pymysql
import json
from connenctions import insert_data , query_data

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="pokemones",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")

data = {}
with open ("python/poke_data.json","r") as json_file:
    data = json.load(json_file)


trainers = []

for pokemon in data:
    values = " (" + str(pokemon["id"]) + " , \"" + pokemon["name"] +"\" , \"" +pokemon["type"] + "\", "+ str(pokemon["height"])+ " ," + str(pokemon["weight"]) + ")"
    insert_data("pokemon",values)
    

    trainers_dict = query_data("SELECT * from trainer")
    for trainer in trainers_dict:
        trainers.append(trainer["name"])

    
    for trainer in pokemon["ownedBy"]:
        if trainer["name"] not in trainers:
            insert_data("trainer", " (\"" + trainer["name"] + "\", \"" +trainer["town"] + "\" )" )
        insert_data("trainer_of_pokemon" , " (" + str(pokemon["id"]) + ", \"" + trainer["name"] + "\" )")

# print(query_data("select * from pokemon"))
