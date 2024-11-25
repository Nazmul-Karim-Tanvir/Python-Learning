# parent class is the base class
# child class is the derived class


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

# child class inherits the properties and methods of the parent class


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
x.welcome()


# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
