import json


def json_serializer(file_name, players):
    with open(file_name, 'w') as f:
        json.dump(players, f)
        f.close()


player_dict = {'Anna': 10000, 'Barney': 9000, 'Jane': 8000, 'Fred': 7000}

json_serializer('json_highscores.txt', player_dict)

