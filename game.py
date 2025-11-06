from core.player import Player
from core.orc import Monster,Orc
from core.goblin import Goblin
import random

class Game:

    def start(self):
        print('wellcome')

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

    def battle(self,player:Player, monster:Orc|Goblin):
        speed_player = player.speed() + roll_dice(6)
        speed_monster = monster.speed() + roll_dice(6)

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
            shoot = roll_dice(20) + first.power()
            if shoot > second.armor_rating():
                injury = calculate_damage(first,second)
                second.hp -= injury
                if  not is_alive(second.hp):
                    return
            else:
                first , second = first,second

def is_alive(hp):
    if hp <= 0 :
        return False
    return True
def calculate_damage(validity:Player | Orc | Goblin, attacked:Player | Orc | Goblin):
    damage = validity.power() + roll_dice(6)
    if isinstance(validity,Monster):
        weapon = validity.weapon()
        damage *= damage_weapon(weapon)
        return damage
def damage_weapon(weapon):
    weapons = ['Knife', 'Sword', 'Axe']
    if weapon == weapons[0]:
        return 0.5
    elif weapon == weapons[1]:
        return 1
    else:
        return 1.5

# def start_queue(player_1, player2):






def roll_dice(sides):
    return random.randint(1, sides)


def get_name_user():
    while True:
        user_name = input('enter your name').strip()
        if user_name.isalpha():
            return user_name
