import keyboard
import time
import sys

def move():
    time.sleep(3)
    keyboard.press('s')
    keyboard.press('a')
    keyboard.press('k')
    keyboard.release('k')
    keyboard.release('s')
    keyboard.release('a')
    keyboard.press(';')
    keyboard.release(';')

move()