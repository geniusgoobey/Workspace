import tkinter as tk

main_window = tk.Tk()

main_window.geometry("500x500")

north_lbl = tk.Label(main_window, text="North")
north_lbl.pack()

west_lbl = tk.Label(main_window, text="West")
west_lbl.pack(side=tk.LEFT)

east_lbl = tk.Label(main_window, text="East")
east_lbl.pack(side=tk.RIGHT)

south_lbl = tk.Label(main_window, text="South")
south_lbl.pack(side=tk.BOTTOM)

main_window.mainloop()