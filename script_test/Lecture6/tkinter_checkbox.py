import tkinter as tk

main_window = tk.Tk()

main_window.geometry("250x125")

# Why I set value in StringVar.
# https://stackoverflow.com/questions/40684739/why-do-tkinters-radio-buttons-all-start-selected-when-using-stringvar-but-not-i
pepperoni_var = tk.StringVar(value="None")
sausage_var = tk.StringVar(value="None")
pineapple_var = tk.StringVar(value="None")

pepp_cb = tk.Checkbutton(main_window, text="Pepperoni", variable=pepperoni_var, onvalue="Pepperoni", offvalue="None")
sausage_cb = tk.Checkbutton(main_window, text="Sausage", variable=sausage_var, onvalue="Sausage", offvalue="None")
pineapple_cb = tk.Checkbutton(main_window, text="Pineapple", variable=pineapple_var, onvalue="Pineapple", offvalue="None")

# When any of the checkbuttons get turned on or off, the corresponding string variable objects
# will be set to the respective state value (onvalue and offvalue).
label1 = tk.Label(main_window, textvariable=pepperoni_var)
label2 = tk.Label(main_window, textvariable=sausage_var)
label3 = tk.Label(main_window, textvariable=pineapple_var)

label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
label3.grid(row=2, column=1)
pepp_cb.grid(row=3, column=0)
sausage_cb.grid(row=3, column=1)
pineapple_cb.grid(row=3, column=2)

main_window.mainloop()