import random

from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon(input("Enter robots weapon"), random.randomint(1, 10))
        

    def attack_opp(self,dinosaur):
        pass