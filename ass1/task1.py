TAX_PERCENTAGE = 0.035  # 3.5% tax


def read_positive_float(prompt: str) -> float:
    """Read a positive float from the user. Keep asking until valid."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
            if value <= 0:
                print("[WARNING] Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("[WARNING] That doesn't look like a valid number.")


def money(x: float) -> str:
    """Format number as money with € and two decimals."""
    return f"{x:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def print_bill(length: float, width: float, price_per_sqm: float) -> None:
    """Prints a simple, formatted price breakdown."""
    area = length * width
    net = area * price_per_sqm
    tax = net * TAX_PERCENTAGE
    gross = net + tax

    print("\n" + "=" * 46)
    print("PROPERTY PRICE BREAKDOWN".center(46))
    print("=" * 46)
    print(f"{'Length:':<20}{length:.2f} m")
    print(f"{'Width:':<20}{width:.2f} m")
    print(f"{'Area:':<20}{area:.2f} m²")
    print(f"{'Price per m²:':<20}{money(price_per_sqm)}")
    print("-" * 46)
    print(f"{'Net price:':<20}{money(net)}")
    print(f"{'Tax (3.5%):':<20}{money(tax)}")
    print("-" * 46)
    print(f"{'Gross price:':<20}{money(gross)}")
    print("=" * 46)


def main():
    print("=== Rectangle Price Calculator ===")
    length = read_positive_float("Enter the length (m): ")
    width = read_positive_float("Enter the width (m): ")
    price_per_sqm = read_positive_float("Enter the price per m² (€): ")

    print_bill(length, width, price_per_sqm)


if __name__ == "__main__":
    main()
