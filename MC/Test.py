import tkinter as tk
import threading
import pyautogui
import time
import sys
from datetime import datetime
import keyboard

def start_function():
    global running
    running = True
    while running:
        time.sleep(1)
        keyboard.release('ctrl')
        move()
        sell()
        keyboard.press('ctrl')
        time.sleep(float(czas))

def move():
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

def sell():
    pyautogui.press('/')
    time.sleep(0.1)
    pyautogui.press('s')
    time.sleep(0.1)
    pyautogui.press('k')
    time.sleep(0.1)
    pyautogui.press('l')
    time.sleep(0.1)
    pyautogui.press('e')
    time.sleep(0.1)
    pyautogui.press('p')
    time.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.move(-33, -133, duration=1)
    pyautogui.click(button='left')
    time.sleep(1)

    pyautogui.click(button='right')
    pyautogui.move(33, 100, duration=1)
    pyautogui.click(button='right')

    pyautogui.move(0, -100, duration=1)
    pyautogui.click(button='right')
    pyautogui.move(0, 100, duration=1)
    pyautogui.click(button='left')

    time.sleep(1)
    pyautogui.press('escape')

def stop_function():
    keyboard.release('ctrl')
    global running
    running = False

def start_thread():
    thread = threading.Thread(target=start_function)
    thread.start()

def update_counter():
    current_time = datetime.now() - start_time
    hours, remainder = divmod(current_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    counter_label.config(text=time_string)
    root.after(1000, update_counter)

def save_variable():
    global czas
    czas = entry.get()

root = tk.Tk()
root.title("AFK")
root.geometry("200x300")
root.configure(bg="black")

root.lift()
root.attributes('-topmost', True)

counter_label = tk.Label(root, text="0:00", width=10, bg="black", fg="white", font=("Arial", 10))
counter_label.pack(pady=10)

start_time = datetime.now()
update_counter()

if root.attributes('-fullscreen'):
    root.attributes('-fullscreen', False)

running = False

# Pole tekstowe
entry = tk.Entry(root, width=10, bg="white", fg="black", font=("Arial", 10))
entry.pack(pady=10)

# Przycisk "Zapisz"
save_button = tk.Button(root, text="Zapisz", command=save_variable, width=10, bg="black", fg="white", font=("Arial", 10))
save_button.pack(pady=10)

# Przycisk "Start"
start_button = tk.Button(root, text="Start", command=start_thread, width=10, bg="green", fg="white", font=("Arial", 10))
start_button.pack(pady=10)

# Przycisk "Stop"
stop_button = tk.Button(root, text="Stop", command=stop_function, width=10, bg="red", fg="white", font=("Arial", 10))
stop_button.pack(pady=10)

root.mainloop()