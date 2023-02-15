import random
import time


def wait_for_enter():
    while True:
        fromuser = input()

        if fromuser == '':
            break


def waiting_game():
    # pick random time between 2 and 4 secs
    waittime = random.randint(2, 4)

    # prompt user
    print(f'Your target time is {waittime} seconds')
    input('--- Press Enter to Begin ---')
    starttime = time.perf_counter()

    input(f'...Press Enter again after {waittime} s')
    elapsedtime = round((time.perf_counter() - starttime), 3)
    print(f'Elapsed time = {elapsedtime}')

    delta = elapsedtime - waittime
    if (delta > 0):
        print(f'{delta :.3f} to fast')
    elif (delta < 0):
        print(f'{-delta :.3f} to slow')
    else:
        print('Wow! Perfect!!!!')


if __name__ == '__main__':
    waiting_game()
