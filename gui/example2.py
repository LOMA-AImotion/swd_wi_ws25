import tkinter as tk
from tkinter import simpledialog


class TaskItem:
    def __init__(self, master, app, text):
        self.app = app
        self.text = text
        self.done = False

        # one row per task
        self.frame = tk.Frame(master)
        self.frame.pack(fill="x", pady=2)

        # left: done button
        self.done_btn = tk.Button(self.frame, text="✓", width=3, command=self.toggle_done)
        self.done_btn.pack(side="left")

        # middle: label
        self.label = tk.Label(self.frame, text=text, anchor="w")
        self.label.pack(side="left", fill="x", expand=True, padx=5)

        # right: edit + delete buttons
        self.edit_btn = tk.Button(self.frame, text="Edit", width=5, command=self.edit)
        self.edit_btn.pack(side="right", padx=2)

        self.delete_btn = tk.Button(self.frame, text="X", width=3, command=self.delete)
        self.delete_btn.pack(side="right")

    def toggle_done(self):
        self.done = not self.done
        if self.done:
            self.label.config(fg="gray", font=("TkDefaultFont", 9, "overstrike"))
        else:
            self.label.config(fg="black", font=("TkDefaultFont", 9, "normal"))

    def edit(self):
        new_text = simpledialog.askstring("Edit task", "Task:", initialvalue=self.text)
        if new_text:
            self.text = new_text
            self.label.config(text=new_text)

    def delete(self):
        self.frame.destroy()
        if self in self.app.tasks:
            self.app.tasks.remove(self)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do")

        self.tasks = []

        # input row
        top = tk.Frame(root)
        top.pack(fill="x", padx=10, pady=10)

        self.entry = tk.Entry(top)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.add_task_event)

        add_btn = tk.Button(top, text="Add", command=self.add_task)
        add_btn.pack(side="left", padx=5)

        # where tasks go
        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        item = TaskItem(self.tasks_frame, self, text)
        self.tasks.append(item)
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
