import os


def deserialize(file_name, players):
    with open(file_name, 'r') as f:
        for entry in f:
            split = entry.split(',')
            name = split[0]
            score = int(split[1])

            players[name] = score


def main():
    players = {}
    file_name = r'highscores2.txt'
    deserialize(file_name, players)
    print(players)


if __name__ == "__main__":
    main()
