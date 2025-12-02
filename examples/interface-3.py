import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")


# Create window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Buttons
tk.Button(root, text="+", width=5, command=lambda: calculate("+")).grid(row=2, column=0)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).grid(row=2, column=1)
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).grid(row=3, column=0)
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).grid(row=3, column=1)

# Result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
