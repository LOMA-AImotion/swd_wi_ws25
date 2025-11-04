factors = [1, 2, 3]
print(f"factors: {factors}")

n = int(input("Multiply by: "))
result = list(map(lambda x: x * n, factors))
print(result)
