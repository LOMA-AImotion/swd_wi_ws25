"""
a1_task2_fancy.py
Converts dog years into equivalent human years.
Includes simple input validation and clear output.
"""


def read_non_negative_int(prompt: str) -> int:
    """Read a non-negative integer (0 or more)."""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("[WARNING] Please enter a valid non-negative number.")
            continue
        value = int(raw)
        return value


def convert_dog_to_human_years(dog_years: int) -> int:
    """Convert dog years to human years using a simple rule set."""
    if dog_years == 0:
        return 0
    elif dog_years == 1:
        return 14
    elif dog_years == 2:
        return 22
    else:
        return 22 + ((dog_years - 2) * 5)


def main():
    print("=== Dog Years to Human Years Converter ===")
    dog_age = read_non_negative_int("How old is your dog (in years)? ")

    human_age = convert_dog_to_human_years(dog_age)

    print("-" * 50)
    print(f"{dog_age} dog years are equivalent to {human_age} human years.")
    print("-" * 50)


if __name__ == "__main__":
    main()
