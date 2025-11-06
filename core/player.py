from abc import ABC, abstractmethod
import random

class Entity(ABC):
    @abstractmethod
    def __init__(self,name , hp = 50):
        self.name = name
        self.hp = hp
    @abstractmethod
    def speed(self):
        pass
    @abstractmethod
    def power(self):
        pass
    def armor_rating(self):
        pass
    @abstractmethod
    def speak(self):
        print(self.name,end=' ')
        pass
    @abstractmethod
    def attack(self):
        pass



class Player(Entity):
    professions = ['Warrior', 'Doctor']

    def __init__(self,name):
        super().__init__(name)
        self.profession = self._profession()

    def _profession(self):
        pro = random.choice(self.professions)
        if pro == self.professions[1]:
            self.hp += 10
        return pro

    def get_profession(self):
        return self.profession

    def speed(self):
        return random.randint(5,10)

    def power(self):
        addition =0
        if self.get_profession() == self.professions[0]:
            addition += 2
        return random.randint(5,10) +addition

    def armor_rating(self):
        return random.randint(5,15)

    def speak(self):
        super().speak()
        print(f'say hi')

    def attack(self):
        pass
# k = Player('koko')
# print(k.power(),k.get_profession())
# k.speak()
# class Any:
#     def __init__(self,name):
#         self.name = name
# class Dog(Any):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#     def s(self):
#         print(21)
# s = Dog('sd',123)
