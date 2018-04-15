class Player:
    def __init__(self, name):
        self.name = name
        self.nums = (2, 4, 6, 8, 10)
    def total(self):
        return sum(self.nums)

play = Player("Raja")
print(play.name)
print(play.nums)

play1 = Player("Ravi")
play1.nums = (2, 4, 6, 8, 10) # if we change this tupple we will get false while checking line 17
play2 = Player("Raj")

print (play1.name == play2.name)
print (play1.nums == play2.nums)

##Second class example

class Student:
    def __init__(self, name, college):
        self.name = name
        self.college = college
        self.marks = []
    def average(self):
        return sum(self.marks) /len(self.marks)

    def goto_schooll(self):
        print ("I am gointo to {}.".format(self.college))
    # class method
    @classmethod
    def goto_school(cls):
        print ("I am going to college")
    @staticmethod
    def goto_school_stat():
        print ("I am going to college")


raj = Student("Raj", "AnnaUniv")
raj.marks.append(75)
raj.marks.append(85)
raj.marks.append(95)
print (raj.marks)
print (raj.average())