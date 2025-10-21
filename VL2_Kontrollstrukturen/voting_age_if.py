print("Hallo, Benutzer!")
age = int(input("Wie ist dein Alter?"))

voting_age = 18
voter_years = age - voting_age

if age < voting_age:
    print("Entschuldigung, du darfst leider noch nicht wählen :(")
    print(f"Du musst leider noch {abs(voter_years)} Jahre warten.")
elif age == voting_age:
    print("Herzlichen Glückwunsch, du darfst bald zum ersten Mal wählen!")
else:
    satz = " Sie dürfen seit " + str(voter_years) + " Jahren wählen."
    print(satz)
