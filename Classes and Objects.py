#Classes and Objects
class Student():
    #Constructor
    def __init__(self, name, age, height, year):
        self.name = name
        self.age = age
        self.height = height
        self.year = year
        self.marks = []

    def displayDetails(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.year)
        print(self.marks)

#Creating Objects
studentDetail = Student('Aryan', 12, '160 cm', 8)
studentDetail.displayDetails()