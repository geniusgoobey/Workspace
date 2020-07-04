import tkinter as tk
import tkinter.ttk as ttk

def submit(selection):
    popup_window = tk.Tk()
    msg = tk.Message(popup_window, width=500)
    if selection == "Python":
        msg.config(text="print('Hello, World!')")
    elif selection == "Rust":
        msg.config(text="fn main(){\n    println!('Hello, World!');\n}")
    elif selection == "Java":
        msg.config(text='public class Test {\n    public static void main(String args[]) { \
                        \n        System.out.println("Hello, World!");\n    }\n}')
    elif selection == "Php":
        msg.config(text='<?php echo "Hello, World!" ?>')
    elif selection == "C++":
        msg.config(text='#include <iostream>\nusing namespace std;\n\nint main(){\n    cout << "Hello, World!";\n}')
    elif selection == "Perl":
        msg.config(text='print "Hello, World!";')
    else:
        msg.config(text=f"{selection} is not a valid option.")
    msg.pack()
    popup_window.mainloop()

main_window = tk.Tk()
selected_var = tk.StringVar(value="Choose one")
cmb_box = ttk.Combobox(main_window, textvariable=selected_var, values=sorted(["Python", "Rust", "Java", \
                                                                               "Php", "C++", "Perl"]))
cmb_box.pack()

#I could use ttk.Button but this demonstrates the ability to combine widgets from
#different modules
submit_btn = tk.Button(main_window, text="Submit", command=lambda: submit(selected_var.get()))
submit_btn.pack()

main_window.mainloop()