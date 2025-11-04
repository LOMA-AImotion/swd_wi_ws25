person = ("Martina", "Musterfrau", 31, True)
person2 = ("Max", "Mustermann", 34, False)

first_name, name, age, joins = person

person_list = [person, person2]

# print(name)

for first_name, name, age, joins in person_list:
    print(f"First name: {first_name}, Age: {age}")