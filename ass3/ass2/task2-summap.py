words = []
k = int(input("Number of words? "))
for i in range(k):
    word = str(input(f"Enter word {i + 1}: "))
    words.append(word)
total = sum(map(len, words))

print(total)
