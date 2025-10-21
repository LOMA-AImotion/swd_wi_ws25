friends = ["Rick", "Carl", "Daryl", "Maggie"]

for friend in friends:
    print(f"Hello {friend}!")
    print(f"(Type of friend: {type(friend)})")

print(10*"-")

mixed_list = ["Rick", 3, 1.25, False]
for element in mixed_list:
    print(f"Current element: {element}")
    print(f"Type of current element: {type(element)}")

print(10*"-")

print(mixed_list)
mixed_list.append(10)
print(mixed_list)

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in nested_list:
    for column in row:
        print(column)