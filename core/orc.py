from core.player import Entity
import random

class Monster(Entity):
    def __init__(self,name,hp,type):
        super().__init__(name,hp)
        self.type = type

    def speed(self):
        pass

    def power(self):
        pass

    def armor_rating(self):
        pass

    def weapon(self):
        weapons = ['Knife', 'Sword', 'Axe']
        return random.choice(weapons)

    def speak(self):
        super().speak()
        print(self.type,end=' ')

    def attack(self):
        pass


class Orc(Monster):
    def __init__(self, name,hp = 50, type = 'orc'):
        super().__init__(name,hp , type)

    def speed(self):
        return random.randint(0,5)

    def power(self):
        return random.randint(10,15)

    def armor_rating(self):
        return random.randint(2,8)

    def attack(self):
        pass

