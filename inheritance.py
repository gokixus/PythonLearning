class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person.")
        
    def eat(self):
        print("I am a eating.")
        
class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Stundent Created")
        
    def who_am_i(self):
        print("I am a student")
        
p1 = Person("Ali", "Yılmaz")
p2 = Student("Çınar", "Turan", 1234)

print(p1.firstName + " " + p1.lastName)
print(p2.firstName + " " + p2.lastName + " " + str(p2.studentNumber))

p1.who_am_i()
p2.who_am_i() 
p1.eat()
p2.eat()
