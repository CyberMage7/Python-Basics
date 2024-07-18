class Student:
    clg_name = "JIIT Sec-62"             #Class Attribute same for all objects
    def __init__(self, first, last):     #self is the object created of class
        print("Constructor is being created")
        self.first = first               #object attributes
        self.last = last

    def greet(self):
        print("Hello,", self.first)


s1 = Student("Vishwas", "Mishra")
print(s1.first + " " + s1.last)
s1.greet()
print("College:", s1.clg_name)

s2 = Student("Anshul", "Kansal")
print(s2.first + " " + s2.last)
s2.greet()
print("College:", s1.clg_name)
