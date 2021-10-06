import random

from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon(input("Enter robots weapon"), random.randomint(1, 10))
        

    def attack_dinosaurs(self,dinosaur):
        if self.health == 0:
           print("{self.name} is out of health and can't attack!")
        else:
            dinosaur.health_points -= self.weapon.attack_power