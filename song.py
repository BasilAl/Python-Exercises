import time
try:
    from winsound import Beep
except:
    pass


def play():

    Beep(440, 500)
    # time.sleep(0.1)
    Beep(440, 500)
    # time.sleep(0.1)
    Beep(440, 500)
    # time.sleep(0.1)
    Beep(349, 400)
    # time.sleep(0.1)
    Beep(523, 350)
    # time.sleep(0.1)
    Beep(440, 600)
    # time.sleep(0.1)
    Beep(349, 400)
    # time.sleep(0.1)
    Beep(523, 350)
    # time.sleep(0.1)
    Beep(440, 1000)
    time.sleep(0.5)

    Beep(659, 500)
    # time.sleep(0.1)
    Beep(659, 500)
    # time.sleep(0.1)
    Beep(659, 500)
    # time.sleep(0.1)
    Beep(698, 400)
    # time.sleep(0.1)
    Beep(523, 250)
    # time.sleep(0.1)
    Beep(415, 500)
    # time.sleep(0.1)
    Beep(349, 400)
    # time.sleep(0.1)
    Beep(523, 250)
    # time.sleep(0.1)
    Beep(440, 1000)
    time.sleep(2)


if __name__ == "__main__":
    print("Playing song(Unmute windows sounds - won't run in other OS)...")
    play()
# 12 seconds
