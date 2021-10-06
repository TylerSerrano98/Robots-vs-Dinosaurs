from robot import Robot

class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.species = name
        self.health_points= 100
        self.attack_power = int(attack_power)
        pass

    def attack(self, robot):
        pass