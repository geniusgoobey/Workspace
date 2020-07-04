import tkinter as tk
    
def flip_switch(canv_obj, btn_text):
    if btn_text == 'on':
        canv_obj.config(bg="#F1F584")
    else:
        canv_obj.config(bg="#000000")
        
main_window = tk.Tk()

light = tk.Canvas(main_window, bg="#000000", width=100, height=50)
light.pack()

on_btn = tk.Button(main_window, text="ON", command=lambda: flip_switch(light, 'on'))
on_btn.pack()

off_btn = tk.Button(main_window, text="OFF", command=lambda: flip_switch(light, 'off'))
off_btn.pack()


#Start our window
main_window.mainloop()