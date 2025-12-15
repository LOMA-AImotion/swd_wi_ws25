
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def show_results(area, price, tax, total):
    print(f"Area: {area:.2f} m²")
    print(f"Price: {price:.2f} €")
    print(f"Tax: {tax:.2f} €")
    print(f"Total: {total:.2f} €")
