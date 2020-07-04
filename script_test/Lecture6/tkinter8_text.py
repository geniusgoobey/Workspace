import tkinter as tk

def display_text(text_widget):
    entered_text = text_widget.get("1.0", tk.END)
    popup_window = tk.Tk()
    label = tk.Label(popup_window, text=f"You entered:")
    label.pack()
    #Message is a mutliline label
    entered_msg = tk.Message(popup_window, text=f"{entered_text}")
    entered_msg.pack()
    popup_window.mainloop()
    

main_window = tk.Tk()
main_window.geometry("150x125")

# Default Text widget width and height are quite big so setting them here.
# Width is 15 characters wide and height is 5 characters tall
text = tk.Text(main_window, width=15, height=5)
text.pack()

submit_btn = tk.Button(main_window, text="Submit", command=lambda: display_text(text))
submit_btn.pack()

main_window.mainloop()