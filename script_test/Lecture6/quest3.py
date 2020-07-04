import tkinter as tk
from tkinter import messagebox as msgBox
    
def submit(username, password):
    if password == 'jumping jama' and username == 'CookieM':
        msgBox.showinfo("Login Successful", "You'll find the cookies under the bed")

main_window = tk.Tk()


u_text = tk.StringVar()
p_text = tk.StringVar()

credentials_frame = tk.Frame(main_window,)

buttons_frame = tk.Frame(main_window)
buttons_frame.grid(row=1, column=3)

u_label = tk.Label(credentials_frame, text="Username:")
u_label.grid(row=0, column=0)

u_entry = tk.Entry(credentials_frame, textvariable=u_text)
u_entry.grid(row=0, column=1)

p_label = tk.Label(credentials_frame, text="Password:")
p_label.grid(row=1, column=0)

p_entry = tk.Entry(credentials_frame, textvariable=p_text, show="*")
p_entry.grid(row=1, column=1)

submit_btn = tk.Button(buttons_frame, text="Submit", command=lambda: submit(u_text.get(), p_text.get()))
submit_btn.pack(side=tk.RIGHT)

main_window.mainloop()