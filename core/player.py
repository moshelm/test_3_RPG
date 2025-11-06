from abc import ABC, abstractmethod
import random

class Entity(ABC):
    @abstractmethod
    def __init__(self,name , hp ):
        self.name = name
        self.hp = hp

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def power(self):
        pass

    @abstractmethod
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

    def __init__(self,name,hp =50):
        super().__init__(name,hp)
        self.profession = self._profession()

    def _profession(self):
        pro = random.choice(self.professions)
        if pro == self.professions[1]:
            self.hp += 10
        return pro
    # help function
    def get_profession(self):
        return self.profession

    def speed(self):
        return random.randint(5,10)

    def power(self):
        addition =0
        if self.get_profession() == self.professions[0]:
            addition += 2
        return random.randint(5,10) + addition

    def armor_rating(self):
        return random.randint(5,15)

    def speak(self):
        super().speak()
        print(f'say hi')

    def attack(self):
        pass
