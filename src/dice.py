from random import randint


class Dice:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]

    def __str__(self):
        s = ""
        for i, d in enumerate(self.dice):
            s += "[" + str(i+1) + "]: " + str(d) + "\n"
        return s

    def get(self):
        return self.dice

    def roll(self):
        for i in range(5):
            self.dice[i] = randint(1, 6)

    def reroll(self, to_be_rerolled: list):
        for i in to_be_rerolled:
            if 1 <= i <= 5:
                self.dice[i-1] = randint(1, 6)
