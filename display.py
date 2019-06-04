import time
import random
import os


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


disp = {0: "    ========================================\n\
    ||   !!!WELCOME TO THE SOS GAME!!!    ||\n\
    ========================================"}
a = "    ========================================\n\
    ||   !!!WELCOME TO THE SOS GAME!!!    ||\n\
    ========================================"
# 54-82


def display(t=12):
    '''Play animation for [t] seconds.
    timers optimised for 12-29 seconds for the 3 given songs.'''
    if t < 12:
        t = 12
    for i in range(1, 30):  # generate 30 labels
        disp[i] = a.replace(a[random.randint(54, 82)], " ")
    for i in a:  # 6.7 seconds
        time.sleep(0.05)
        print(i, end="", flush=True)
    for i in range(int((t-6.7)/(0.1))):
        time.sleep(0.06)
        clear()
        print(disp[random.randint(1, 29)])
    clear()
    print(disp[0])
    time.sleep(0.5)


if __name__ == "__main__":
    display(random.randint(12, 29))
