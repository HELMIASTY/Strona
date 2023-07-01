import pyautogui
import keyboard
import tkinter as tk
import threading
import sys
import time

root = tk.Tk()
root.title('Fast peeck')
# root.geometry("100x100")
root.configure(bg="black", cursor="crosshair")
root.lift()
root.attributes('-topmost', True)

def astra():
    global x, y
    x = 720
    y = 1230

def pick():
    while not keyboard.is_pressed('space'):
        pyautogui.moveTo(x, y)
        pyautogui.click(button="left")
        pyautogui.moveTo(1290, 1085)
        pyautogui.click(button="left")
    pass

#Napis
text = tk.Label(root, text="Wybierz postać, a potem naciśnij pick", bg="black", fg="white", font=("Arial", 10))
text.pack(pady=10)

#pick
pick = tk.Button(root, command=pick, text="PICK", bg="green", fg="white", font=("Arial", 10))
pick.pack(pady=10)

#Postacie
astra = tk.Button(root, command=astra, text="Astra", bg="black", fg="white", font=("Arial", 10))
astra.pack(pady=1)

# breach = tk.Button(root, command=breach, text="Breach", bg="black", fg="white", font=("Arial", 10))
# breach.pack(pady=1)

# brimstone = tk.Button(root, command=brimstone, text="Brimstone", bg="black", fg="white", font=("Arial", 10))
# brimstone.pack(pady=1)

def exit(event):
    if event.keysym == 'escape':
        root.quit()

root.bind('<KeyPress>', exit)

root.mainloop()