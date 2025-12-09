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

    file = open(path_to_file)
    lines = file.readlines()
    file.close()
    
    num_overall_questions = int(lines[0].strip())


    all_questions = list()
    
    # each question consists of 5 lines 
    for i in range(1, (num_overall_questions)*5, 5):
        question_text = lines[i]
        all_answers = [lines[i+j] for j in range(1, 5)]
        
        correct_index = 0
        # search answers for CORRECT: tag and extract the question
        for index, text in enumerate(all_answers):
            if text.startswith("CORRECT:"): # this must be the correct answer 
                text = text.replace("CORRECT:", "")    
                all_answers[index] = text
                correct_index = index 
                
        # Update correct answer; It should be displayed without the CORRECT: tag.
        question = (question_text, all_answers[0], all_answers[1], all_answers[2], all_answers[3], correct_index)
        all_questions.append(question)

    return all_questions
    

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

    question_pool = [question for question in all_questions if  question != current_question]
    
    return random.choice(question_pool)
 

if __name__ == "__main__":
    questions = load_questions_from_file("/Users/lodes/Work/git/swd_wi_ws25/VL8_Quiz/quiz_functions.txt")