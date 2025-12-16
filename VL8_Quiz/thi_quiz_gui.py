# -*- coding: utf-8 -*-
"""
thi_quiz_gui.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

import tkinter as tk
# Sometimes the explicit import is necessary
from tkinter import messagebox
#from tkinter import ttk
from functools import partial

# Its not necessary to declare the global variables twice, but it adds
# some more explicity and improves visibility of these variables
correct_index = None
all_questions = None
get_next_question_fn = None

path_to_image = None 
# path_to_image = "quiz_logo.png"
# Depending on your IDE, you may need to pass an explicit path
# path_to_image = "C:\path\to\image\quiz_logo.png"
options = "ABCD"
# options = "1234"


def answered(i):
    """
    Compares the given answer with the solution. 

    Args:
        i: integer, the index (starting at 0) of the given answer.
    """

    print(f"I got the answer {i}")
    if i == correct_index:
        # Sometimes the explicit call is necessary
        tk.messagebox.showinfo("Well done", "That is indeed correct, congrats.")
        draw_gui() # Reload GUI with new question
    else:
        tk.messagebox.showerror("Try again", "That was not correct, try again.")



def draw_gui():
    """
    Retrieves the next question and updates the texts in the GUI.    
    """
    global correct_index

    # Here we actually call the stored function reference
    question = get_next_question_fn(all_questions)
    question_text, a1, a2, a3, a4, correct_idx = question
    answers = [a1, a2, a3, a4]
    
    correct_index = correct_idx # We can only access, but not modify global variables!
    
    question_label.config(text=question_text)
    
    for i, button in enumerate(answer_buttons): 
        # convert i to row and col index
        button.config(text=f"{options[i]}) {answers[i]}") 

main_window:tk.Tk = tk.Tk()
main_window.title("THI Quiz")

# this holds our logo
logo_tk = tk.PhotoImage(file=path_to_image)
logo_label = tk.Label(main_window, image = logo_tk)
logo_label.grid(row = 0, column = 0, columnspan = 2)

question_label = tk.Label(main_window, text="Hello!", font=("Arial 18 bold"))
question_label.grid(row=1, column=0, columnspan=2)

answer_buttons = [tk.Button(main_window, text=f"Answer {i}") for i in range(4)]

button_index = 0
for i in range(2,4):
    for j in range(0,2):
        current_button = answer_buttons[button_index]
        current_button.config(command=partial(answered, button_index))
        current_button.grid(row= i, column=j)

        button_index += 1

