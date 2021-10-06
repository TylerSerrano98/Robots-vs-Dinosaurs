from robot import Robot

class Fleet:

    def __init__(self):
        self.create_robots = []

    def create_fleet(self):
        while len(self.create_robots) < 3:
            self.create_robots.append(Robot(input("Enter name of bot")))