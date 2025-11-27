import tkinter as tk

window = tk.Tk()
window.title("My First GUI")

label = tk.Label(window, text="Hello Tkinter!")
label.pack()

window.mainloop()
