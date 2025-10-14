print("Hallo, Benutzer!")
age = int(input("Wie ist dein Alter?"))

voting_age = 18
voter_years = age - voting_age

satz = " Sie dürfen seit " + str(voter_years) + " Jahren wählen."
print(satz)
