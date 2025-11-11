k = int(input("Up to which k should I build the set? "))

result_set = set()

for i in range(1, k+1):
    result_set.add((i, i*"x"))

print(result_set)