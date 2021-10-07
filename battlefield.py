import random

from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.user_team = ''
        self.users_characters = None
        self.users_targets = None
        self.user_attack = None
        self.target_attack = None
        self.user_defend = None
        self.target_defend = None
        self.user_selector = 0
        self.target_selector = 0
        self.target = 0


    def run_game(self):
        self.display_welcome()
        self.team_select()

    def team_select(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.user_team = input('Choose "dinosaurs" or "robots"')
        while(self.user_team != 'dinosaurs') and (self.user_team != 'robots'):
            self.user_team = input('Not a team: Pick "dinosaurs" or "robots')
        if self.user_team == 'dinosaurs':
            self.users_characters = self.herd.dinosaur
            self.users_targets = self.fleet.robot
            print("\nYou're team of dinos is:")
            for dinosaur in self.users_characters:
                print(f'Species: {dinosaur.species}, Health: {dinosaur.health_points}, Attack Power: {dinosaur.attack_power}')
            print("Here is your enemy robots:")
            for robot in self.users_targets:
                print(f'Name: {robot.name}, Health: {robot.health}, Weapon: {robot.weapon.weapon_type} (atk) {robo.weapon.attack_power}')         
        else:
            self.user_team = self.fleet.robot
            self.users_targets = self.herd.dinosaur
            print("\nYou're team of robots is:")
            for robot in self.users_characters:
                print(f'Name: {robot.name}, Health: {robot.health}, Weapon: {robot.weapon.weapon_type} (atk) {robot.weapon.attack_power}')
            print("Here is your enemy dinosaurs:")
            for dinosaur in self.users_targets:
                print(f'Species: {dinosaur.species}, Health: {dinosaur.health_points}, Species: {dinosaur.species}')


    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs")

    def battle(self):
        pass

    def dino_turn(self):
        if self.users_characters == self.herd.dinosaur:
            self.user_attack = self.users_characters[self.user_selector]
            print(f"\nYou're attacking character is: Species: {self.user_attack.species}, Health: {self.user_attack.health_points}, Attack Power: {self.user_attack.attack_power}")
            print(f'\nPick a target to attack!\n')
            self.show_robo_opponent_options()
            self.target_selector = int(input("Enter enemy number:"))
            while (self.target_selector < 0) or (self.target_selector > len(self.users_targets) - 1):
                self.target_selector = int(input("not an enemy: please select an enemy number"))
            self.target_defend = self.users_targets[self.target_selector]
            print(f"\n{self.user_attack.species} hits {self.target_defend.name} for {self.user_attack.attack_power} health points!")
            self.user_attack.attack(self.target_defend)
            if self.user_selector >= (len(self.users_characters)-1):
                self.user_selector = 0
            else:
                self.user_selector += 1
        else:
           self.target = random.randint(0, len(self.user)-1)
           self.target_attack = self.users_targets[random.randint(0, len(self.enemy)-1)]
           self.user_defend = self.users_characters[self.target]
           print(f"\n{self.target_attack.species} attacks {self.user_defend.name} for {self.target_attack.attack_power} health points")
           self.target_attack.attack(self.user_attack)
           if self.user_selector >= (len(self.users_characters)-1):
               self.user_selector = 0

    def show_robo_opponent_options(self):
        for robot in self.users_targets:
            print(f'Enter "{self.target_selector}" Name: {robot.name}, Health: {robot.health}, Weapon: {robot.weapon.weapon_type} (atk) {robot.weapon.attack_power}')
            self.target_selector += 1
        
    
    def robo_turn(self):
        if self.users_characters == self.fleet.robot:
            self.user_attack = self.users_characters[self.user_selector]
            print(f"\nYou're attacking character is: Name: {self.user_attack.name}, Health: {self.user_attack.health}, Weapon: {self.user_attack.weapon.weapon_type} (atk) {self.user_attack.weapon.attack_power}")
            print(f'\nPick a target to attack!\n')
            self.show_dino_opponent_options()
            self.target_selector = int(input("Enter enemy number:"))
            while (self.target_selector < 0) or (self.target_selector > len(self.users_targets) - 1):
                self.target_selector = int(input("not an enemy: please select an enemy number"))
            self.target_defend = self.users_targets[self.target_selector]
            print(f"\n{self.user_attack.name} hits {self.target_defend.species} for {self.user_attack.weapon.attack_power} health points!")
            self.user_attack.attack(self.target_defend)
            if self.user_selector >= (len(self.users_characters)-1):
                self.user_selector = 0
            else:
                self.user_selector += 1
        else:
            self.target = random.randint(0, len(self.user)-1)
            self.target_attack = self.users_targets[random.randint(0, len(self.enemy)-1)]
            self.user_defend = self.users_characters[self.target]
            print(f"\n{self.target_attack.species} attacks {self.user_defend.name} for {self.target_attack.attack_power} health points")
            self.target_attack.attack(self.user_attack)
            if self.user_selector >= (len(self.users_characters)-1):
                    self.user_selector = 0
        

    def show_dino_opponent_options(self):
        for dinosaur in self.users_targets:
            print(f'Enter "{self.target_selector}" Species: {dinosaur.species}, Health: {dinosaur.health_points}, Attack Power: {dinosaur.attack_power}')
            self.target_selector += 1

    def display_winners(self):
        pass