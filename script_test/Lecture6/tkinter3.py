import tkinter as tk

main_window = tk.Tk()

main_window.geometry("150x100")

label1 = tk.Label(main_window, text="Label 1")
label1.place(x=40, y=50)

label2 = tk.Label(main_window, text="Label 2")
label2.place(x=40, y=50)

main_window.mainloop()