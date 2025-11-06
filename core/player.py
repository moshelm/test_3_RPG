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
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def armor_rating(self):
        pass

class Player(Entity):
    def __init__(self,name,hp):
        super().__init__(name,hp)
        self.profession = self._profession()
    def _profession(self):
        professions = ['Warrior','Doctor']
        return random.choice(professions)
    def speed(self):
        return random.randint(5,10)
    def power(self):
        return random.randint(5,10)
    def armor_rating(self):
        return random.randint(5,15)
    def speak(self):
        print(f'{self.name} say hi')
    def attack(self):
        pass

class Any:
    def __init__(self,name):
        self.name = name
class Dog(Any):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def s(self):
        print(21)
s = Dog('sd',123)
