import tkinter as tk

def change(entry, should_display):
    if should_display:
        entry.config(show="")
    else:
        entry.config(show="*")
        
main_window = tk.Tk()
main_window.resizable(False, False)
entry_frame = tk.Frame(main_window)

label = tk.Label(entry_frame, text="Entry")

word_entry = tk.Entry(entry_frame, bg="black", fg="red")

btn_frame = tk.Frame(main_window)

show_btn = tk.Button(btn_frame, text="Show", command=lambda: change(word_entry, True))

hide_btn = tk.Button(btn_frame, text="Hide", command=lambda: change(word_entry, False))

#Frame using Grid manager
label.grid(row=0, column=0)
word_entry.grid(row=0, column=1)

#Frame using Pack manager
show_btn.pack(side=tk.LEFT)
hide_btn.pack(side=tk.RIGHT)

#Main Frame using pack manager
entry_frame.pack(fill=tk.X)
btn_frame.pack(fill=tk.X)

main_window.mainloop()