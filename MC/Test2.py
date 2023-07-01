import keyboard
import time
import sys

def exit():
    sys.exit()

def move():
    while True:
        if keyboard.is_pressed('q'):
            keyboard.press('s')
            keyboard.press('a')
            time.sleep(2)
            keyboard.release('s')
            keyboard.release('a')
            time.sleep(0.2)

            keyboard.press('d')
            time.sleep(0.1)
            keyboard.release('d')
            keyboard.press('w')
            time.sleep(0.7)
            keyboard.release('w')
            keyboard.press('d')
            time.sleep(0.7)
            keyboard.release('d')
            keyboard.press('s')
            time.sleep(0.7)
            keyboard.release('s')
            keyboard.press('a')
            time.sleep(0.7)
            keyboard.release('a')

            keyboard.press('d')
            time.sleep(0.25)
            keyboard.release('d')
            keyboard.press('w')
            time.sleep(0.5)
            keyboard.release('w')
            keyboard.press('d')
            time.sleep(0.2)
            keyboard.release('d')
            keyboard.press('s')
            time.sleep(0.2)
            keyboard.release('s')
            keyboard.press('a')
            time.sleep(0.15)
            keyboard.release('a')
            keyboard.press('w')
            time.sleep(0.15)
            keyboard.release('w')

            exit()


move()