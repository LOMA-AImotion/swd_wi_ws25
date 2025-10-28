sum = 0
max_number = 1

k = int(input("What is my budhget?"))

while sum + (max_number**2) <= k:
    sum = sum + (max_number**2)
    # equivalent: max_number += 1
    max_number = max_number + 1
    
print(f"The sum is {sum}, the largest number I can fit is {max_number-1}")
