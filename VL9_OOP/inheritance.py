class Person:
  def __init__(self, name):
        self.name = name

  def greet(self):
        print(f"***** Hi, my name is {self.name}")

class Student(Person):
    def __init__(self, name, matriculation_id):
        super().__init__(name)
        self.matriculation_id = matriculation_id
    
    def greet(self):
        print(f"***** Hi, my name is {self.name} and my matriculation number is {self.matriculation_id}")

p = Person("Caroline")
s = Student("Francis", 14483)

list_of_persons = [p, s]

for person in list_of_persons:
    person.greet()
        
        
