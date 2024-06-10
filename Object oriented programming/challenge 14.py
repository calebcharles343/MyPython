# Function or method overriding

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('HI, i am just a ' + self.name)


class PoliceRobot(Robot):
    def say_hi(self):
        print('Hi, this is the ' + self.name + ' Robot. Here to help!')


r = Robot('Robot')
r.say_hi()

pr = PoliceRobot('police')
pr.say_hi()