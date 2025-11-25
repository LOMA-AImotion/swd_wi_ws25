import tkinter

main_win = tkinter.Tk()
main_win.title("WI SWD")
label = tkinter.Label(main_win, text="My first GUI")
label.pack()

button = tkinter.Button(main_win, text="OK")
button.pack()
main_win.mainloop()

print("Hello from after mainloop()")
