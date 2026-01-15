

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        if not title.strip() or not author.strip() or not isbn.strip():
            raise ValueError("Title, author and isbn should not be empty")
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Book (title: {self.title}, author: {self.author}, isbn: {self.isbn})"
    
    def get_details(self):
        return self.__str__()
    
    


book = Book(title="The Hobbit", author="J.R.R. Tolkien", isbn="978-0618260300")
print(book)
print(book.get_details())



class Library:
    def __init__(self, name="A random library"):
        self.all_books = []
        self.name = name
    
    def add_book(self, book: Book):
        self.all_books.append(book)

    def get_details(self):
        if len(self.all_books) == 0:
            print(f"{self.name}: Library is empty")
            return
        print(self.name + ": ")
        for book in self.all_books:
            details = book.get_details()
            print(f"\t{details}")


lib = Library(name="Library@THI")


lib.add_book(book)
lib.add_book(Book(title="The Hobbit2", author="J.R.R. Tolkien", isbn="9718-0618260300"))
lib.get_details()

lib2 = Library(name="Library@THI-ND")
lib2.get_details()



print(Book(title="The Hobbit2", author="J.R.R. Tolkien", isbn="9718-0618260300").get_details())

# constructorcall -> function() -> create Instance -> on instance we can call instance functions (methods)