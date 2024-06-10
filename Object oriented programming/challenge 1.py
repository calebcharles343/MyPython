from random import *


# Dice

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

dice1 = Dice(6)
print(dice1.roll_dice())
print(dice1.roll_dice())