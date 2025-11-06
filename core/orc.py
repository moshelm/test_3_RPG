from player import Entity
import random
from abc import ABC

class Monster(Entity):
    def __init__(self,name,hp,type):
        super().__init__(name,hp)
        self.type =type

    def speed(self):
        pass
    def power(self):
        pass

    def speak(self):
        pass

    def attack(self):
        pass

    def armor_rating(self):
        pass

class Orc(Monster):
    def __init__(self, name, hp, type = 'orc'):
        super().__init__(name, hp, type)

    def speed(self):
        return random.randint(0,5)
    def power(self):
        return random.randint(10,15)
    def armor_rating(self):
        return random.randint(2,8)
    def speak(self):
        print(f'{self.name} {self.type}')
    def attack(self):
        pass