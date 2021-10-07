from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.user_team = ''
        self.users_characters = None
        self.users_targets = None



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
            print("/nYou're team of dinos is:")
            for dinosaur in self.users_characters:
                print(f'Species: {dinosaur.species}, Health: {dinosaur.health_points}, Species: {dinosaur.species}')
            print("Here is your enemy robots:")
            for robot in self.users_targets:
                print(f'Name: {robot.name}, Health: {robot.health}, Weapon: {robot.weapon.weapon_type}')         
        else:
            self.user_team = self.fleet.robot
            self.users_targets = self.herd.dinosaur
            print("/nYou're team of robots is:")
            for robot in self.users_characters:
                print(f'Name: {robot.name}, Health: {robot.health}, Weapon: {robot.weapon.weapon_type}')
            print("Here is your enemy dinosaurs:")
            for dinosaur in self.users_targets:
                print(f'Species: {dinosaur.species}, Health: {dinosaur.health_points}, Species: {dinosaur.species}')


    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs")

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass