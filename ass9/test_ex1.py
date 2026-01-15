"""
Exercise 1 – Testing and Debugging (Clean Version with Test Functions)

- Each part has its own test function.
- Each test has a clear description.
- Uses plain `assert` (no extra libraries).
"""

# ------------------------------------------------------------
# a) Strategy to identify logically incorrect code
# ------------------------------------------------------------
"""
Simple strategy for finding logic errors:

1) State the goal in one sentence (what should the code do?).
2) Pick a tiny example and compute the expected result by hand.
3) Run the code and compare with the expected result.
4) Test edge cases (first element, last element, empty input, etc.).
5) Print intermediate values (or use a debugger) to see where behavior changes.
6) Fix one issue, then re-run the same tests.
"""


# ------------------------------------------------------------
# b) Fixed vector_addition
# ------------------------------------------------------------
def vector_addition(vectorA: list[float], vectorB: list[float]) -> list[float]:
    """Return element-wise sum of two vectors (lists) of equal length."""
    if len(vectorA) != len(vectorB):
        raise ValueError("Both vectors must have the same length.")

    result = [0] * len(vectorA)
    for i in range(len(vectorA)):  # correct: start at 0
        result[i] = vectorA[i] + vectorB[i]
    return result


# ------------------------------------------------------------
# c) Fixed calculate_overall_price
# ------------------------------------------------------------
def calculate_overall_price(area: float, price_per_sqm: float = 40, tax: float = 0.15) -> float:
    """Return total price including tax."""
    net_price = area * price_per_sqm
    return net_price * (1 + tax)  # correct: total including tax


# ------------------------------------------------------------
# Small helpers for clean testing output
# ------------------------------------------------------------
def check(description: str, condition: bool) -> None:
    """Assert with a readable description."""
    assert condition, f"❌ Test failed: {description}"
    print(f"✅ {description}")


def check_raises(description: str, expected_exception: type[Exception], func) -> None:
    """Check that calling func() raises expected_exception."""
    try:
        func()
    except expected_exception:
        print(f"✅ {description}")
        return
    except Exception as e:
        assert False, (
            f"❌ Test failed: {description}\n"
            f"   Raised different exception: {type(e).__name__}"
        )
    assert False, f"❌ Test failed: {description}\n   No exception was raised."


def check_close(description: str, actual: float, expected: float, eps: float = 1e-9) -> None:
    """Check two floats are approximately equal (handles floating-point rounding)."""
    check(description, abs(actual - expected) < eps)


def test_vector_addition() -> None:
    print("\n--- Tests for vector_addition ---")

    # Catches the original bug: skipping index 0
    check(
        "Adds all elements including the first element (index 0)",
        vector_addition([1, 2], [10, 20]) == [11, 22]
    )

    check(
        "Handles negative and positive numbers correctly",
        vector_addition([0, -1, 5], [7, 1, -2]) == [7, 0, 3]
    )

    check(
        "Works with empty vectors",
        vector_addition([], []) == []
    )

    check_raises(
        "Raises ValueError when vectors have different lengths",
        ValueError,
        lambda: vector_addition([1, 2, 3], [1, 2])
    )


def test_calculate_overall_price() -> None:
    print("\n--- Tests for calculate_overall_price ---")

    # Catches the original bug: net_price * tax (returns only tax amount)
    check_close(
        "Returns net*(1+tax) (not net*tax)",
        actual=calculate_overall_price(100, 2, 0.10),
        expected=220.0
    )

    # Catches the calling mistake: forgetting to pass tax (would use default 0.15)
    area = 500
    price_per_sqm = 85
    tax = 0.10
    expected_total = area * price_per_sqm * (1 + tax)

    check_close(
        "Uses the provided tax argument (not the default tax)",
        actual=calculate_overall_price(area, price_per_sqm, tax),
        expected=expected_total
    )

    check_close(
        "Uses default values correctly (price_per_sqm=40, tax=0.15)",
        actual=calculate_overall_price(10),
        expected=10 * 40 * 1.15
    )


def run_all_tests() -> None:
    test_vector_addition()
    test_calculate_overall_price()
    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_all_tests()

    # Demo: printing with 2 digits after the decimal point
    area = 500
    price_per_sqm = 85
    tax = 0.10
    overall_price = calculate_overall_price(area, price_per_sqm, tax)
    print(f"\nDemo output: The overall price is {overall_price:.2f}")
