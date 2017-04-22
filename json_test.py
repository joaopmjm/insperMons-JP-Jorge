import os
import sys
import jsonpickle


game_state = dict(batata = 4)

Inspermon_save = "Inspermon_save.json"

def save_game():

    global game_state
    with open(Inspermon_save, 'w') as save:
        save.write(jsonpickle.encode(game_state))

def load_game():

    try:
        with open(Inspermon_save, 'r') as save:
            file = jsonpickle.decode(save.read())
        return file
        pass
    finally:
        pass