import random
class Hero():
    #
    def __init__(self, name='', level=50, score=0):
        self.name = name
        self.level = int(level)
        self.score = int(score)

    def __str__(self):
        return "The hero's name is {0}. {0}'s ability level is {1}".format(self.name, self.level)

    def attack(self, opponent):
        hero_roll = random.randint(1, 6) * self.level
        opponent_roll = random.randint(1, 6) * opponent.level
        if hero_roll >= opponent_roll:
            return True
        else:
            return False

class Opponent():
    #
    def __init__(self, name, level):
        self.name = name
        self.level = int(level)

    def __str__():
        return "The opponent's name is {0}. {0}'s ability level is {1}".format(self.name, self.level)
