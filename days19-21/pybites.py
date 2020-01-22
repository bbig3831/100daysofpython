from itertools import permutations, combinations, zip_longest

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return permutations(friends, team_size)
    else:
        return combinations(friends, team_size)


if __name__ == '__main__':
    get_attendees()