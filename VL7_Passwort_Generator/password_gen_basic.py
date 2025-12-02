import random
import tkinter as tk
import string

# Paths maybe absolute or relative - depends on how you execute the script
adjectives_path = "/Users/lodes/Work/git/swd_wi_ws25/pw_gen_sol/adjektive.txt"
nouns_path = "/Users/lodes/Work/git/swd_wi_ws25/pw_gen_sol/nomen.txt"


def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        cleaned_lines = [line.rstrip() for line in lines]
    
    return cleaned_lines

def generate_password():
    adjectives = read_file(adjectives_path)
    nouns = read_file(nouns_path)

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 100)
    sc = random.choice(string.punctuation)

    password = f"{adjective}{noun}{number}{sc}"
    password_label.config(text=password) 
    return password


# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place the Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(root, text="Generated PW: ")
password_label.pack()

root.mainloop()
