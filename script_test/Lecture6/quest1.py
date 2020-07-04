#Python 3
import tkinter as tk
from tkinter import messagebox as msgBox
from functools import partial
 
pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["C", 0, "S"]]
passcode = ""

def append_passcode(value):
    global passcode
    if len(passcode) == 4:
        passcode = passcode[1:]
    passcode += value

def clear():
    global passcode
    passcode = ""
    
def submit(attempt, secret):
    global passcode
    if(passcode!=""):
        if attempt == secret:
            msgBox.showinfo("Login Attempt", "Successful")
            passcode = ""
        else:
            msgBox.showinfo("Login Attempt", "Failed")
            passcode = ""

main_window = tk.Tk()

btns = []
row_placement = 0
for line in pad:
    col_placement = 0
    for number in line:
        btn_command = partial(append_passcode, str(number))
        btn = tk.Button(main_window, text=number, width=10, command=btn_command)
        btns.append(btn)
        btn.grid(row=row_placement, column=col_placement)
        col_placement += 1
    row_placement += 1
  

#Setting C to clear the passcode function
btns[-3].config(command=clear)

#Setting S to submit passcode
btns[-1].config(command=submit(passcode, "1234"))

main_window.mainloop()