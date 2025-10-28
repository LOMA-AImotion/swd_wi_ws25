mt = [0, 1, 4, 5, 7, 8]

differences = [mt[i] - mt[i - 1] for i in range(1, len(mt))]
print(differences)