import tkinter
from tkinter.messagebox import showinfo

def say_hi():
    showinfo("Info", "Hi!")

main_win = tkinter.Tk()
button = tkinter.Button(main_win, text="Say Hi",
                        command = say_hi)
button.pack()
main_win.mainloop()

