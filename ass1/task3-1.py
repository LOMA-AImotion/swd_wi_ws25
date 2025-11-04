year = int(input("Which year do you want to check? "))

# Leap year rule:
# - divisible by 4 -> leap year
# - except if divisible by 100 -> not a leap year
# - unless also divisible by 400 -> leap year again
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")
