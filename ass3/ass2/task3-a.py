char = str(input("What symbol? "))
n = int(input("Number of times? "))
l = []
for i in range(n):
    l.append((i + 1) * char)
print(l)
