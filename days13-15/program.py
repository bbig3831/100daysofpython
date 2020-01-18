import random

from actors import Creature, Dragon, Wizard

def main():
    print_header()
    game_loop()

def print_header():
    print('--------------------------------')
    print('          WIZARD GAME           ')
    print('--------------------------------')
    print()

def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'The wizard defeated {active_creature.name}')
            else:
                print('The wizard has been dealt a defeat!')
        elif cmd =='r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f'*  {c.name} of level {c.level}')
            print()
        else:
            print('OK, exiting the game...bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

if __name__ == '__main__':
    game_loop()