class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname): #could override Person's __init__
    Person.__init__(self, fname, lname) #but actually calls Person's __init__
    #super().__init__(fname, lname) #or use this to automatically inherit the 
    # parent class properties without naming the parent class

x = Student("Mike", "Olsen")
x.printname()