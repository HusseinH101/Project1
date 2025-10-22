import random

class Dice:
    
    def __init__(self, sides=6):
        """""This function initializes the the methods"""
        self.sides = sides

    def roll(self):
        """""This functions rolls a dice and returns
        a random number from 1-6"""
        return random.randint(1, self.sides)
