import pyautogui
import keyboard
import tkinter as tk
import threading
import sys

def exit_program():
    sys.exit()

def klik():
    acction = 0
    while True:
        if keyboard.is_pressed('z'):
            if acction == 0:
                acction = 1
            if acction == 2:
                acction = 3
        if acction == 1:
            pyautogui.mouseDown(button='left')
            acction = 2
        if acction == 3:
            pyautogui.mouseUp(button='left')
            acction = 0

root = tk.Tk()
root.title("Kliker")
root.geometry("200x200")
root.configure(bg="black")

# Przycisk zamykający program
exit_button = tk.Button(root, text="Zamknij", command=exit_program, width=20, height=10, bg="black", fg="white", font=("Arial", 10))
exit_button.pack(pady=10)

# Uruchomienie funkcji działającej w tle w oddzielnym wątku
background_thread = threading.Thread(target=klik)
background_thread.daemon = True
background_thread.start()


root.mainloop()