def Driver(car):
    car.drive()

class Creta:
    def drive(self):
        print('Creta is driving')
class Mercedes:
    def drive(self):
        print('Mercedes is driving')

c1 = Creta()
Driver(c1)

c2 = Mercedes()
Driver(c2)
print('########################################')

def PetLover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is talking')
    def walk(self):
        print('Duck is walking')
class Dog:
    def talk(self):
        print('Dog is talking')
    # def walk(self):
        # print('Dog is walking')

d1 = Duck()
PetLover(d1)

d2 = Dog()
PetLover(d2)