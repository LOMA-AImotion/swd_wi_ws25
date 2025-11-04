data = []


def printStatistics():
    lengths = list(map(len, data))
    min_len, max_len, mean_len = min(lengths), max(lengths), sum(lengths) / len(lengths)
    print(f"min: {min_len}, max: {max_len}, mean: {mean_len}")


while True:
    name = str(input(f"Please enter a string {len(data) + 1}: "))
    if name.casefold() == "stop":
        printStatistics()
        break
    data.append(name)
