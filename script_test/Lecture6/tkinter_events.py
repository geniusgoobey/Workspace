
import tkinter as tk

def keyrec_callback(event):
    if event.char:
        if event.char == '\t':
            event.widget.config(text='<TAB>')
        elif event.char == ' ':
            event.widget.config(text='<SPACE>')
        elif event.char == '\r':
            event.widget.config(text='<ENTER>')
        elif event.char == '\x08':
            event.widget.config(text='<BACKSPACE>')
        else:
            event.widget.config(text=event.char)
            
main_window = tk.Tk()

label = tk.Label(main_window, text="Type Keys")

#<Key> is any key that is displayable.  Special keys such as Enter or Alt will result in an empty value
label.bind('<Key>', keyrec_callback)
label.pack()

# Set the focus to the label when you focus on the application
label.focus_set()

main_window.mainloop()