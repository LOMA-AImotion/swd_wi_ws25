data = [1, 2, 3]

fst = []
scd = []


def isFirst(n: int) -> bool:
    return n % 2 == 0


for entry in data:
    if isFirst(entry):
        fst.append(entry)
    else:
        scd.append(entry)

print(f"\t Inital {data}")
print("\t/ \t\t \\")
print(f"\t{fst} \t\t {scd}")
