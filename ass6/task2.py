def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


# Test examples
tests = [
    "anna",
    "Anna",
    "Step on no pets.",
    "Mr. Owl ate my metal worm.",
    "Hello THI"
]

for t in tests:
    print(f"{t} -> {is_palindrome(t)}")
