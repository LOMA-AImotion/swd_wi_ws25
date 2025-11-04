s = "I study at THI and I have fun"
words = s.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
