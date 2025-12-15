## Solutions (in English)

---

### **Task 1 – User Stories (1 Point)**

- As a user, I want to be able to import questions from an Excel file.  
- As a user, I want to be able to create a random quiz from multiple individual quizzes in order to review learning material more effectively.  
- As a user, I want to see statistics about my learning progress in order to evaluate the effectiveness of my learning.  
- As a user, I want to be able to compare my performance with other users to better assess my own performance.  
- As a user, I want to receive graphical feedback indicating whether I answered a question correctly or not.

---

### **Task 2 – Use Cases (2 Points)**

#### **Use Case 1: Evaluate Learning Progress**
1. The user informs the system that they want to evaluate their learning progress.  
2. The system displays the quizzes previously completed by the user.  
3. The user selects the completed quizzes for which detailed statistics should be shown.  
4. The system analyzes the stored results and displays how performance has developed over time.

#### **Use Case 2: Create a Quiz with Multiple Choice Questions**
1. The user starts the quiz creation function.  
2. The system opens the dialog for entering questions.  
3. The user enters a question, the associated answer options, and the correct answer.  
4. The user chooses whether to finish and save the quiz, cancel the input, or add more questions:  
   - i) If the user chooses to finish the quiz, the system asks for a quiz name and saves the quiz under that name.  
   - ii) If the user chooses to cancel, the system asks for confirmation. If confirmed, the dialog is closed without saving.  
   - iii) If the user chooses to enter more questions, the process repeats from step 3.

---

### **Task 3 – Required Tasks (2 Points)**

#### **Required Tasks for Use Case 1: Learning Progress Evaluation**
1. Add functionality (e.g., button or menu item) to the main window to start the statistics dialog.  
2. Develop a GUI that displays completed quizzes and related statistics.  
3. Compute and graphically visualize statistics about the user’s learning progress.

#### **Required Tasks for Use Case 2: Quiz Creation**
1. Add functionality (e.g., button or menu item) to the main window to start the quiz editor.  
2. Develop a GUI that allows the user to enter complete quizzes consisting of individual questions with correct answer options and guides the user through the process.  
3. Implement a function to validate the entered questions with respect to correct format.  
4. Implement a function to persistently save the created quizzes to the local storage.
