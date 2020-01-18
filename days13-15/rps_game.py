import random

ROLLS = ['rock', 'paper', 'scissors']
RULES = {
    'rock':{
        'beats':'scissors'
    },
    'paper':{
        'beats':'rock',
    },
    'scissors':{
        'beats':'paper',
    }
}

class Roll:

    def __init__(self, roll_name):
        self.roll = roll_name

    def can_beat(self, other_roll):
        if RULES.get(self.roll).get('beats') == other_roll.roll:
            return 'win'
        elif self.roll == other_roll.roll:
            return 'tie'
        else:
            return 'lose'


class Player:

    def __init__(self, name):
        self.name = name


def print_header():
    print('-----------------------')
    print('  ROCK-PAPER-SCISSORS  ')
    print('-----------------------')
    print()


def game_loop(player1, player2):
    rolls = {
        player1.name:{
            'rolls':[],
            'score':0
        },
        player2.name:{
            'rolls':[],
            'score':0
        }
    }

    count = 1
    while count < 4:
        p2_roll = Roll(roll_name=random.choice(ROLLS))
        inp = input('Make your selection ({}): '.format('/'.join(ROLLS)))
        p1_roll = Roll(roll_name=inp.lower())

        outcome = p1_roll.can_beat(p2_roll)

        # Display throws
        print(f'{player1.name} threw {p1_roll.roll}')
        print(f'{player2.name} threw {p2_roll.roll}')
        # Display winner for this round
        print(f'{player1.name} {outcome}s!')
        print()

        # Store results
        rolls[player1.name]['rolls'].append(p1_roll.roll)
        rolls[player2.name]['rolls'].append(p2_roll.roll)
        if outcome == 'win':
            rolls[player1.name]['score'] += 1
        elif outcome == 'lose':
            rolls[player2.name]['score'] += 1

        count += 1

    # Compute who won
    print(f"{player1.name} had {rolls[player1.name]['score']} points.")
    print(f"{player2.name} had {rolls[player2.name]['score']} points.")
    print()


def main():
    print_header()

    name = input('What is your name? ')
    player1 = Player(name)
    player2 = Player('computer')

    game_loop(player1, player2)


if __name__ == '__main__':
    main()