import tkinter as tk
from tkinter import messagebox


def add_pair():
    key = entry_key.get().strip()
    value = entry_value.get().strip()

    if key == "":
        messagebox.showerror("Error", "Key cannot be empty!")
        return

    dictionary[key] = value

    entry_key.delete(0, tk.END)
    entry_value.delete(0, tk.END)


def finish():
    messagebox.showinfo("Dictionary Contents", str(dictionary))
    root.destroy()


# Main window
root = tk.Tk()
root.title("Dictionary Input")

dictionary = {}

# Labels
label_key = tk.Label(root, text="Key:")
label_key.grid(row=0, column=0, padx=10, pady=5, sticky="e")

label_value = tk.Label(root, text="Value:")
label_value.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Entry fields
entry_key = tk.Entry(root, width=30)
entry_key.grid(row=0, column=1, padx=10, pady=5)

entry_value = tk.Entry(root, width=30)
entry_value.grid(row=1, column=1, padx=10, pady=5)

# Buttons
button_add = tk.Button(root, text="Add", command=add_pair)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_finish = tk.Button(root, text="Finish", command=finish)
button_finish.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
