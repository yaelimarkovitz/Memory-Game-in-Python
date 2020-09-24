from .connenctions import insert_data, query_data

def insert_trainer(trainer):
    # trainers = []
    # trainers_dict = query_data("SELECT * from trainer")
    # for trainer in trainers_dict:
    #     trainers.append(trainer["name"])
    insert_data( "trainer", " (\"{}\", \"{}\")".format(trainer["name"], trainer["town"]))

def insert_trainer_of_pokemon(trainer,pokemon):
    insert_data( "trainer_of_pokemon" , " (" + str(pokemon) + ", \"" + (trainer) + "\" )")