from robot import Robot

class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.species = name
        self.health_points= 100
        self.attack_power = int(attack_power)
        pass

    def attack(self, robot):
        if self.health_points == 0:
            print(f"{self.species} is out of HP and can't attack!")
        else:
             robot.health -= self.attack_power