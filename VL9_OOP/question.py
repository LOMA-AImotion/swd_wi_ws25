class Question:
    def __init__(self, question, alternatives, correct):
        self.question = question
        self.alternatives = alternatives
        self.correct = correct
        self.correct_index = alternatives.index(correct) # derived information
  
    def is_correct(self, answer):
	    return self.correct == answer


q1 = Question("What is 2+2?", ["2", "5", "4", "3"], "4")
q2 = Question("What is 2+3?", ["2", "5", "4", "3"], "5")

print(f"Is 5 correct for q1? {q1.is_correct("5")}")
print(f"Is 5 correct for q2? {q2.is_correct("5")}")
