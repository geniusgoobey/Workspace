import tkinter as tk

def display(event):
    event.widget.config(foreground="#000")

def hide(event):
    event.widget.config(foreground="#F0F0F0")
    
main_window = tk.Tk()
main_window.title("Welcome")
main_window.geometry("250x100")

welcome_lbl = tk.Label(main_window, text="Welcome to my System")
welcome_lbl.pack()

warning_lbl = tk.Label(main_window, text="Said the spider to the fly", foreground="#F0F0F0")
warning_lbl.bind('<Enter>', display) #Notice, no parenthesis for display, just the name of the function
warning_lbl.bind('<Leave>', hide)  #Same as above line but for hide
warning_lbl.pack(side=tk.BOTTOM)

main_window.mainloop()