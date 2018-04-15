class Student:
    def __init__(self, name, college):
        self.name = name
        self.college = college
        self.marks = []
    def average(self):
        return sum(self.marks) /len(self.marks)
    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.college, *args)

class Working_Student(Student):
    def __init__(self, name, college, salary):
        super(Working_Student, self).__init__(name, college)
        self.salary = salary

raj = Working_Student("Raja", "MIT", 70.00)
print (raj.salary)
frinend = Working_Student.friend(raj, "AnnaUniv", 73.00)
print (frinend.name)
print (frinend.college)
print (frinend.salary)