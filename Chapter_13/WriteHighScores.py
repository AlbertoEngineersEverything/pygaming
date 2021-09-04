import os
players = ['Anna,1000', 'Barney,9000', 'Jane,8000', 'Fred,7000']
f = open('highscores.txt', 'w')
for player in players:
    f.write(player+'\n')

f.close()
