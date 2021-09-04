import os


def serialize(file_name, players):
    with open(file_name, 'w') as f:
        for p in players:
            f.write(p+','+str(players[p])+'\n')


players = {'Anna': 10000, 'Barney': 9000, 'Jane': 8000, 'Fred': 7000}

serialize('highscores2.txt', players)