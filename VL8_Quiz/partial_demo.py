import tkinter
from tkinter import messagebox
from functools import partial

main_win = tkinter.Tk() 
number = 1

def show_info_box(num):
    messagebox.showinfo("Hi", f"You pressed {num}")
    
for row in range(4):
    for col in range(4):
        button = tkinter.Button(main_win, text=str(number))
        button.grid(row=row, column = col)        
        button.config( height = 5, width = 10)
        button.config(command = partial(show_info_box, number))
        number += 1
main_win.mainloop()
