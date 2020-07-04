import tkinter as tk

def order_dinner(listbox_widget):
    selected_index = listbox_widget.curselection()
    
    popup_window = tk.Tk()
    msg_label = tk.Label(popup_window)
    if selected_index:
        selection = listbox_widget.get(selected_index)
        msg_label.config(text=f"You selected {selection}")
    else:
        msg_label.config(text="Nothing selected")
    msg_label.pack()
    popup_window.mainloop()

main_window = tk.Tk()
main_window.title("Dinner Selector")
main_window.geometry("300x200")
choices = ['Pizza', 'Spaghetti', 'Salad', 'PB&J', 'Macaroni and Cheese']

choices_listbox = tk.Listbox(main_window, selectmode=tk.SINGLE)

# To add items to a list box, we need to specify an index and the item.
# enumerate function takes an iterable object and produces a tuple in 
# which the first element is the index of the item in the iterable
# and the second item is the value itself.
for (i, v) in enumerate(choices):
    choices_listbox.insert(i, v)
    
choices_listbox.pack()

submit_btn = tk.Button(main_window, text='Submit', command=lambda: order_dinner(choices_listbox))
submit_btn.pack()

main_window.mainloop()