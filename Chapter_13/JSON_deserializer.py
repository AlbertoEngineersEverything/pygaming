import json


def json_deserializer(file_name):
    with open(file_name, 'r') as f:
        players = json.load(f)
        f.close()
        return players


file_name = r'json_highscores.txt'
player_json = json_deserializer(file_name)

print(player_json)
