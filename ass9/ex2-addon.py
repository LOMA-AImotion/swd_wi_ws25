from __future__ import annotations


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        if not title.strip() or not author.strip() or not isbn.strip():
            raise ValueError("Title, author and isbn should not be empty")
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn})"

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"

    def __eq__(self, other: object) -> bool:
        """Two books are equal if they have the same ISBN."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def get_details(self) -> str:
        return str(self)


class Library:
    def __init__(self, name: str = "A random library"):
        self.all_books: list[Book] = []
        self.name = name

    # ---- requested dunders ----
    def __str__(self) -> str:
        """User-friendly description."""
        if len(self.all_books) == 0:
            return f"{self.name}: Library is empty"
        return f"{self.name}: {len(self.all_books)} book(s)"

    def __len__(self) -> int:
        """Enables len(library)."""
        return len(self.all_books)

    def __iter__(self):
        """Enables: for book in library."""
        return iter(self.all_books)

    def __getitem__(self, index):
        """
        Enables: library[i] and slicing like library[1:3].
        We forward indexing to the underlying list.
        """
        return self.all_books[index]

    def __add__(self, other: Book | "Library") -> "Library":
        """
        Enables:
          new_lib = lib + book
          new_lib = lib + other_lib

        Returns a NEW Library (doesn't modify the old one),
        which is often nice for teaching immutability vs mutability.
        """
        new_lib = Library(name=f"{self.name} (combined)")
        new_lib.all_books = self.all_books.copy()

        if isinstance(other, Book):
            new_lib.all_books.append(other)
            return new_lib

        if isinstance(other, Library):
            new_lib.all_books.extend(other.all_books)
            return new_lib

        return NotImplemented

    # ---- regular methods ----
    def add_book(self, book: Book) -> None:
        self.all_books.append(book)

    def get_details(self) -> None:
        print(str(self))
        for book in self.all_books:
            print(f"\t{book}")  # uses Book.__str__


# ------------------ DEMO / EXAMPLES ------------------

print("=== Creating books ===")
book1 = Book(title="The Hobbit", author="J.R.R. Tolkien", isbn="978-0618260300")
book2 = Book(title="The Hobbit (another copy)", author="J.R.R. Tolkien", isbn="978-0618260300")
book3 = Book(title="The Hobbit 2", author="J.R.R. Tolkien", isbn="9718-0618260300")
print("book1:", book1)
print("book2:", book2)
print("book3:", book3)





print("\n\n\n=== Book equality (__eq__) compares ISBN ===")
print("book1 == book2 ?  (same ISBN)", book1 == book2)
print("book1 == book3 ?  (different ISBN)", book1 == book3)







print("\n\n\n=== Creating libraries ===")
lib = Library(name="Library@THI")
lib2 = Library(name="Library@THI-ND")




print("\n\n\n=== __str__ for Library ===")
print("Printing an empty library:", lib2)







print("\n\n\n=== Adding books (normal method) ===")
lib.add_book(book1)
lib.add_book(book3)
print("After adding 2 books:", lib)  # uses Library.__str__









print("\n\n\n=== __len__ allows len(library) ===")
print(f"len({lib}) =", len(lib))
print(f"len({lib2}) =", len(lib2))






print("\n\n\n=== __iter__ allows looping directly ===")
print("Looping over lib:")
for b in lib:
    print(" -", b)






print("\n\n\n=== __getitem__ allows indexing and slicing ===")
print("lib[0] gives the first book:", lib[0])
print("lib[0:2] gives a list (slice) of books:", lib[0:2])








print("\n\n\n=== __add__ allows combining ===")
print("1) lib + book2 (creates a NEW library, original unchanged)")
lib_plus_one = lib + book2
print("Original lib:", lib, "| len =", len(lib))
print("New lib_plus_one:", lib_plus_one, "| len =", len(lib_plus_one))







print("\n\n\n2) lib + lib2 (combines two libraries into a NEW one)")
combined = lib + lib2
print("combined:", combined, "| len =", len(combined))









print("\n\n\n=== Library.get_details() uses Book.__str__ for each book ===")
lib.get_details()
print("Empty library details:")
lib2.get_details()
