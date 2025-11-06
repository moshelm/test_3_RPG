from core.player import Player
from core.orc import Monster,Orc
from core.goblin import Goblin
import random

class Game:

    def start(self):
        print('wellcome')
        self.show_menu()

    def show_menu(self):
        print('for battle enter 1')
        print('for exit enter 0')

    def create_player(self):
        user_name = get_name_user()
        return Player(user_name)

    def choose_random_monster(self):
        monsters = ['Orc','Goblin']
        choose = random.choice(monsters)
        if choose == monsters[0]:
            return Orc('Bob')
        else:
            return Goblin('Clark')

    def roll_dice(self,sides):
        return random.randint(1, sides)

    def battle(self,player:Player, monster:Orc|Goblin):
        speed_player = player.speed() + self.roll_dice(6)
        speed_monster = monster.speed() + self.roll_dice(6)

        if speed_player > speed_monster:
                first = player
                second = monster
        elif speed_player < speed_monster:
            first = monster
            second = player
        else:
            first = player
            second = monster
        while True:
            shoot = self.roll_dice(20) + first.speed()
            first.speak()
            if shoot > second.armor_rating():
                power = self.roll_dice(6) + first.power()
                damage = calculate_damage(first,power)
                display_status_game(first,second)

                second.hp -= damage
                if  not is_alive(second.hp):
                    print(f'{first.name} you win')
                    return
            else:
                first , second = first,second
                display_status_game(first,second)

def display_status_game(player,monster):
    print(f'{player.name} hp:{player.hp}')
    print(f'{monster.name} hp:{monster.hp}')

def is_alive(hp):
    if hp <= 0 :
        return False
    return True

def calculate_damage(validity:Player | Orc | Goblin, power):
    if isinstance(validity,Monster):
        weapon = validity.weapon()
        power *= damage_weapon(weapon)
        return power
    else:
        return power

def damage_weapon(weapon):
    weapons = ['Knife', 'Sword', 'Axe']
    if weapon == weapons[0]:
        return 0.5
    elif weapon == weapons[1]:
        return 1
    else:
        return 1.5


def get_name_user():
    while True:
        user_name = input('enter your name').strip()
        if user_name.isalpha():
            return user_name
        print('try again')
