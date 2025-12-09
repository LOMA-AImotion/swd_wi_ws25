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
get_next_question = None

path_to_image = "quiz_logo.png" 
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

    pass


def draw_gui():
    """
    Retrieves the next question and updates the texts in the GUI.    
    """

    pass

main_window:tk.Tk = tk.Tk()
main_window.title("THI Quiz")


