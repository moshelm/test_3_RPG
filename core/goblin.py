from orc import Monster
import random
class Goblin(Monster):

    def __init__(self,name , hp = 20 , type= 'goblin'):
        super().__init__(name,hp , type)
    def speed(self):
        return random.randint(5,10)
    def power(self):
        return random.randint(5,10)
    def armor_rating(self):
        return 1
    def weapon(self):
        weapons = ['Knife','Sword','Axe']
        return random.choice(weapons)
    def speak(self):
        print(f'{self.name} {self.type}')
    def attack(self):
        pass