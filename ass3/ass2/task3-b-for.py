factors = [1, 2, 3]
print(f"factors: {factors}")

n = int(input("Multiply by: "))
result = []
for entry in factors:
    result.append(entry * n)
print(result)
