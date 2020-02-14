import sys

import sqlite3
from contextlib import contextmanager


@contextmanager
def access_db():
    try:
        conn = sqlite3.connect()
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()

def add_room():
    name = input()
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute()

def add_inventory():
    pass

def view_inventory():
    pass

def scrub(table_name):
    return ''.join(chr for chr in table_name if chr.isalnum())

def check_input():
    pass


def main_menu():
    menu = {}
    menu['1'] = 'Add room'
    menu['2'] = 'Add inventory'
    menu['3'] = 'View inventory list'
    menu['4'] = 'Total value'
    menu['5'] = 'Exit'