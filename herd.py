import random
from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.create_dinos = []
        

    def create_herd(self):
        while len(self.create_dinos) < 3:
            self.create_dinos.append(Dinosaur(input("Name a species of Dinosaur"))), random.randomint(1, 10)
