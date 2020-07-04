import tkinter as tk

main_window = tk.Tk()
main_window.geometry("150x65")

selection = tk.StringVar(value="None")

opt1 = tk.Radiobutton(main_window, text="Soda", variable=selection, value="Soda")
opt2 = tk.Radiobutton(main_window, text="Pop", variable=selection, value="Pop")

label = tk.Label(main_window, textvariable=selection)

opt1.deselect()
opt2.deselect()

opt1.pack()
opt2.pack()
label.pack()

main_window.mainloop()
