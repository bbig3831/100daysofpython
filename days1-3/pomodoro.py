from datetime import datetime, timedelta
from time import sleep

TIMER_LENGTH = 1

def pomodoro_timer(start_dt):
    """

    :param start_dt:
    :return:
    """
    end_dt = start_dt + timedelta(minutes=TIMER_LENGTH)
    print(f'Starting Pomodoro timer for {TIMER_LENGTH} minutes')
    while datetime.now() < end_dt:
        sleep(60)
        min_left = round((end_dt - datetime.now()).seconds / 60, 2)
        print(f'You have {min_left} minutes left')

    print("Time's up! Take a break.")

if __name__ == '__main__':
    pomodoro_timer(start_dt=datetime.now())