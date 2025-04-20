#Classes and Objects
class Student():
    #Constructor
    def __init__(self, name, age, height, year):
        self.name = name
        self.age = age
        self.height = height
        self.year = year
        self._marks = []

    def displayDetails(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.year)
        print(self._marks)
    
    def updateMarks(self):
        noOfSubjects = int(input('How many subjects does student take?'))
        for i in range(noOfSubjects):

            markForSubject = int(input(f'Enter your mark for Subject {i + 1}: '))
            self._marks.append(markForSubject)

    def markCalculations(self):
        sum = 0
        for eachMark in self._marks:
            sum = sum + eachMark 
        average = sum / len(self._marks)
        print(average)
        print(sum)

    def displayMarks(self):
        for i in self._marks:
            print(i)

#Creating Objects
studentDetail = Student('Aryan', 12, '160 cm', 8)
studentDetail.displayDetails()
studentDetail.updateMarks()
studentDetail.markCalculations()
studentDetail.displayMarks()

#Accessing or Changing the Object
studentDetail.age = 13
print(studentDetail.age)

#studentDetail.marks = ['10', 15, 'happy']
#studentDetail.markCalculations()

#