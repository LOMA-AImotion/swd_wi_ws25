shopping_list = {}

user_response = input("Do you want to add an item (yes/no)? ")

while user_response != "no":
    item = input("Which item do you want to add? ")
    quantity = input("How many do you want to add? ")
    shopping_list[item] = quantity
    user_response = input("Do you want to add an item (yes/no)? ")

print(shopping_list)
print(f"Keys: {shopping_list.keys()}")
print(f"Values: {shopping_list.values()}")
