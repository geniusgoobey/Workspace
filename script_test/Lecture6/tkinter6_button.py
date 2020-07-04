'''import tkinter as tk

def popup():
    popup_window = tk.Tk()
    label = tk.Label(popup_window, text="This is a popup")
    label.pack()
    popup_window.mainloop()

main_window = tk.Tk()

main_window.geometry("200x50")

popup_btn = tk.Button(main_window, text="Click me", command=popup)
popup_btn.pack()

main_window.mainloop()'''

import tkinter as tk
from random import randint

def roll_dice(label):
    label.config(text=f"{randint(1, 6)}")
    
main_window = tk.Tk()

main_window.geometry("100x50")

label = tk.Label(main_window, text="0")
label.pack()

roll_btn = tk.Button(main_window, text="Roll Die", command=lambda: roll_dice(label))
roll_btn.pack()

main_window.mainloop()