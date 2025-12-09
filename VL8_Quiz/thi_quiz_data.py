# -*- co    ding: utf-8 -*-
"""
thi_quiz_data.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

import random

def load_questions_from_file(path_to_file):
    """
    Loads a txt file that contains questions in the format from the lecture.

    Args:
        path to file: String that contains the path to the txt file

    Returns:
        A list that contains all questions from the txt file in the following format:
        [(question, answer1, answer2, answer3, answer4, correct_index), 
        ..., 
        (question, answer1, answer2, answer3, answer4, correct_index)]
    """

    pass


def get_random_question_from_complete_list(all_questions, current_question=None):
    """
    Draws one question from a list and place it back to the pool.

    Args:
        all_questions: list that contains all questions
        current_question: the currently displayed question - if none ignore 

    Returns:
        One single question in the following format: 
        (question, answer1, answer2, answer3, answer4, correct_index)
    """
    pass
 