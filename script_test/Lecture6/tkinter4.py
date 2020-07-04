import tkinter as tk

main_window = tk.Tk()

main_window.geometry("230x100")

for r in range(0, 4):
    for c in range(0, 4):
        tmp_label = tk.Label(main_window, text=f"(r={r}, c={c})")
        tmp_label.grid(row=r, column=c)
        
main_window.mainloop()