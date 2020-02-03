# Avoiding if-elif complexity
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts = dict(zip(days, routines))

def get_workout(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    return routine

# Counting inside a loop
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

for i, day in enumerate(days, 1):
    print(f'{i}. {day}')

# Using the with statement
# with open('text', 'w') as f:
#     f.write('hello\n')
#     raise Exception

# Tuple unpacking and namedtuples
a, b = 1, 2
a, b = b, a

from collections import namedtuple

Workout = namedtuple('Workout', 'routine day duration')
workout = Workout('Chest+biceps', 'Monday', '45')

# List comprehensions and generators
from random import choice

def get_random_day(days=days):
    i = 0
    while True:
        i +=1
        yield i, choice(days)

# PEP8 and Zen
