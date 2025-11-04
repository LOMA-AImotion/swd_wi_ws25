capacity = 10
reserved_spots = 0

user_name = input("Hello, what is your name? ")
requested_spots = int(input("How many spots do you want to book? "))

while reserved_spots < capacity:
    if reserved_spots + requested_spots <= capacity:
        reserved_spots += requested_spots
        # reserved_spots = reserved_spots + requested_spots

        print(f"OK {user_name}, {reserved_spots}/{capacity} are taken, I can accept {capacity - reserved_spots} more.")
    else:
        print("Not enough capacity available, sorry.")

    user_name = input("Hello, what is your name? ")
    requested_spots = int(input("How many spots do you want to book? "))

print("Capacity exhausted, abort program...")
    