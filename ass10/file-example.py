# Hey students, this is a short example for parent and child classes in action
# File is a abstract representation of file, only containing the path and
# two functions open, and get_path NOTE: get_path is implemented and open not
# the reson for that is simple but important
# i) open will need a different implementation for each child class (pdf, html, excel)
# ii) get_path will be the same for parent class and child classes therefore we can 
# implement it once and use it in all child classes 

class File:
    def __init__(self, path: str):
        self.path = path
    
    def open(self):
        pass

    def get_path(self):
        print(self.path)

class ExelFile(File):
    def __init__(self, path: str):
        super().__init__(path)
    
    def open(self):
        print("Lese Excel")
        
class PDFFile(File):
    def __init__(self, path: str):
        super().__init__(path)

    def open(self):
        print("Lese pdf")

class HTMLFile(File):
    def __init__(self, path: str):
        super().__init__(path)

    def open(self):
        print("Lese HTML")

class DOCXFile(File):
    def __init__(self, path):
        super().__init__(path)
    
    def open(self):
        print("Lese Doxc")


file1 = "rechnung.pdf"
file2 = "rechnung.excel"
file3 = "rechnung.html"

all_files = [file1, file2, file3]

for path in all_files:
    # print(path)
    file = None
    if path.endswith(".pdf"):
        file = PDFFile(path)
    if path.endswith(".excel"):
        file = ExelFile(path)
    if path.endswith(".html"):
        file = HTMLFile(path)
    file.open()
    file.get_path()

