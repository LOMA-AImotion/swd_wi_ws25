import tkinter as tk

def show_text():
    print(entry.get())

window = tk.Tk()
window.title("Input Example")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Print", command=show_text)
button.pack()

window.mainloop()
