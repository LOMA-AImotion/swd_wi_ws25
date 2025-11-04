## a

print("-" * 5, " a ", "-" * 5)

customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"],
]
last_names = [person[1] for person in customers]
print(last_names)


ln = []
for p in customers:
    ln.append(p[1])
print(ln)


print("\n\n", "-" * 10, "\n\n")

## b
print("-" * 5, " b ", "-" * 5)
numbers = [1, 4, 2, 8, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number * number)
print(squared_numbers)

result = []
n = [1, 4, 2, 8, 5]
while len(n) > 0:
    current = n.pop(0)
    result.append(current * current)
print(result)


print("\n\n", "-" * 10, "\n\n")
## c
print("-" * 5, " c ", "-" * 5)
import random

secret_number = random.randint(1, 100)  # Generate random number
guess = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Guess again.")
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("You guessed it! The number was", secret_number)

tries = [1]
for i in tries:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Guess again.")
        tries.append(i + 1)
    elif guess < secret_number:
        print("Too low! Guess again.")
        tries.append(i + 1)
    else:
        print("You guessed it! The number was", secret_number)
        print(f"tries: {len(tries) + 1}")
        break


print("\n\n", "-" * 10, "\n\n")
