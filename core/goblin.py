from core.orc import Monster
import random

class Goblin(Monster):
    def __init__(self,name , hp = 20 , type= 'goblin'):
        super().__init__(name,hp,type)

    def speed(self):
        return random.randint(5,10)

    def power(self):
        return random.randint(5,10)

    def armor_rating(self):
        return 1

    def attack(self):
        pass
