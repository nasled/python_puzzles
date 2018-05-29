input = ['amy 100','david 100','heraldo 50','aakansha 75','aleksa 150']

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score > b.score:
            return -1
        return 1


data = []
for i in input:
    name, score = i.split()
    score = int(score)
    player = Player(name, score)
    data.append(player)


data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)