from game import Game
def want_play():
    while True:
        user  = input('enter your chose').strip()
        if user == '1':
            return True
        elif user =='0':
            return False
        print('you can only 0 or 1')

def main():
    a = Game()
    a.start()
    if want_play():
        player = a.create_player()
        monster = a.choose_random_monster()
        a.battle(player,monster)
    else:
        print('goodbye')

if __name__=='__main__':
    main()