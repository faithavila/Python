
# Description of Program: Takes in student name and grades and averages them out on command.
class Student:
    def __init__ (self, name, grade1 = None, grade2 = None):
        self.name = name
        self.__grade1 = (grade1)
        self.__grade2 = (grade2)

    def getName(self):
        return self.name
    
    def getExam1Grade(self):      
        return self.__grade1

    def getExam2Grade(self):
        return self.__grade2

    def setExam1Grade(self, grade1):
        self.__grade1 = (grade1)
    
    def setExam2Grade(self, grade2):
        self.__grade2 = (grade2)

    def getAverage(self):
        if self.__grade1 == None or self.__grade2 == None:
            return "Some exam grades not available."
        else:
            return str(float((float(self.__grade2) + float(self.__grade1)) / 2))
    
    def __str__(self):
        return "Student: " + str(self.name) + "\n  Exam1: " + str(self.__grade1) + "\n  Exam2: " + str(self.__grade2)