symbol = "#"
n = int(input("Size of triangle? "))

for i in range(1, n * 2):
    print(symbol * (i if i <= n else 2 * n - i))
