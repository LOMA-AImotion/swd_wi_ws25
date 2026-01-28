import tkinter as tk
from tkinter import simpledialog

tasks = []
LEFT_CLICK = "<Button-1>"

def on_done_click(event):
    btn = event.widget
    task = btn.task
    task["done"] = not task["done"]

    if task["done"]:
        task["label"].config(fg="gray", font=("TkDefaultFont", 9, "overstrike"))
    else:
        task["label"].config(fg="black", font=("TkDefaultFont", 9, "normal"))


def on_edit_click(event):
    btn = event.widget
    task = btn.task

    new = simpledialog.askstring("Edit task", "Task:", initialvalue=task["text"])
    if new:
        task["text"] = new
        task["label"].config(text=new)


def on_delete_click(event):
    btn = event.widget
    task = btn.task
    task["frame"].destroy()
    tasks.remove(task)


def add_task():
    text = entry.get().strip()
    if not text:
        return

    frame = tk.Frame(tasks_frame)
    frame.pack(fill="x", pady=2)

    # ---- Buttons and label ----
    done_btn = tk.Button(frame, text="Done?", width=3)
    done_btn.pack(side="left")

    label = tk.Label(frame, text=text, anchor="w")
    label.pack(side="left", fill="x", expand=True, padx=5)

    edit_btn = tk.Button(frame, text="Edit", width=5)
    edit_btn.pack(side="right", padx=2)

    delete_btn = tk.Button(frame, text="X", width=3)
    delete_btn.pack(side="right")

    # ---- Task dictionary ----
    task = {
        "frame": frame,
        "label": label,
        "text": text,
        "done": False
    }
    tasks.append(task)

    # Attach task reference to buttons
    done_btn.task = task
    edit_btn.task = task
    delete_btn.task = task

    # Bind clicks ( Could also be done with lambda, 
    # but used the simple representation as lambda isnt a big part of the lecture)
    done_btn.bind(LEFT_CLICK, on_done_click)
    edit_btn.bind(LEFT_CLICK, on_edit_click)
    delete_btn.bind(LEFT_CLICK, on_delete_click)

    entry.delete(0, tk.END)


# ---- UI ----
root = tk.Tk()
root.title("To-Do")

top = tk.Frame(root)
top.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(top)
entry.pack(side="left", fill="x", expand=True)

add_btn = tk.Button(top, text="Add", command=add_task)
add_btn.pack(side="left", padx=5)

tasks_frame = tk.Frame(root)
tasks_frame.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
