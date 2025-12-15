from datetime import datetime
import time


def time_until(target: datetime) -> str:
    """Return a string with the time remaining until 'target'."""
    now = datetime.now()
    diff = target - now
    # Just return the difference, even if it's negative
    return str(diff)


def main():
    # Target dates (midnight at the start of the day)
    christmas_eve = datetime(2024, 12, 24, 0, 0, 0)
    new_year = datetime(2025, 1, 1, 0, 0, 0)
    easter_2025 = datetime(2025, 4, 20, 0, 0, 0)

    while True:
        print("Till Christmas eve:", time_until(christmas_eve))
        print("Till new year:     ", time_until(new_year))
        print("Till easter:       ", time_until(easter_2025))
        print("---------------")
        time.sleep(1)


if __name__ == "__main__":
    main()

