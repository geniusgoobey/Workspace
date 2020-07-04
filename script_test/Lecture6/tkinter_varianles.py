import tkinter as tk

def submit(strvar, intvar, dblvar, chbtnvar):
    popup_window = tk.Tk()
    tk.Label(popup_window, text=f"Your stringvar contained {strvar}").pack()
    tk.Label(popup_window, text=f"10 + {intvar} = {intvar + 10}").pack()
    tk.Label(popup_window, text=f"{dblvar} celcius is {(dblvar*1.8)+32} fahreinheit").pack()
    tk.Label(popup_window, text=f"{'ON' if chbtnvar else 'OFF'}").pack()
    popup_window.mainloop()
    

main_window = tk.Tk()

str_var = tk.StringVar()
int_var = tk.IntVar()
dbl_var = tk.DoubleVar()
bln_var = tk.BooleanVar()

tk.Label(main_window, text="Enter a string:").grid(row=0, column=0)
tk.Label(main_window, text="Enter an int:").grid(row=1, column=0)
tk.Label(main_window, text="Enter a double:").grid(row=2, column=0)
tk.Label(main_window, text="Turn on/off:").grid(row=3, column=0)

str_entry = tk.Entry(main_window, textvariable=str_var)
int_entry = tk.Entry(main_window, textvariable=int_var)
dbl_entry = tk.Entry(main_window, textvariable=dbl_var)

#Notice, instead of text variable, I am using variable for Checkbutton widget.
bln_chbtn = tk.Checkbutton(main_window, variable=bln_var)

str_entry.grid(row=0, column=1)
int_entry.grid(row=1, column=1)
dbl_entry.grid(row=2, column=1)
bln_chbtn.grid(row=3, column=1)

submit_btn = tk.Button(main_window, text="Submit", command=lambda: submit(str_var.get(), int_var.get(),dbl_var.get(), bln_var.get()))
submit_btn.grid(row=4, column=1)

main_window.mainloop()