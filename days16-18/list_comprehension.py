from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

names = 'pybites mike bob julian tim sara guido'.split()
first_half_alphabet = list(string.ascii_lowercase)[:13]
test = [name.title() for name in names if name[0] in first_half_alphabet]

# Harry Potter text
resp = requests.get('https://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
words = [re.sub(r'\W+', r'', word) for word in words]

# Stop words
resp = requests.get('https://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
words = [word for word in words if word.strip() and word not in stopwords]

cnt = Counter(words)
cnt.most_common(5)

# Generators
def num_gen():
    for i in range(5):
        yield i

gen = num_gen()
next(gen)
for i in gen:
    print(i)

options = 'red yellow blue white black green purple'.split()

def gen_options(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'

list(gen_options())

# Performance
def leap_years_list(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year

