symbol = "#"

n = int(input("Size of triangle? "))

for index in range(n * 2 - 1):
    if index <= n - 1:
        print(symbol * (index + 1))
    else:
        print(symbol * (n - (index % n + 1)))
