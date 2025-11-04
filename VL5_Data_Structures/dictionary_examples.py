example_dict = {
    "A": 1, 
    "key": "value"
}

example_dict["B"] = 2

print(example_dict["B"])

print(example_dict.get("C", "Key is not in dictionary :("))