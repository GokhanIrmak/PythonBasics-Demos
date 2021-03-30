class Student():
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return self.firstname+ " " + self.lastname

#Inheriting Student
class WorkingStudent(Student):
    def __init__(self,firstname,lastname,company):
        super().__init__(firstname,lastname)
        self.company = company


w_student = WorkingStudent("John","Doe","EC")
student=Student("Monica","Miller")

#Instance Type
print(type(w_student))
print(type(student))

if type(student) == Student:
    print("Only non-working Students")
elif type(w_student) == WorkingStudent:
    print("Only working Students")

#Instance IsInstance
#Check if given variable is instance of given type
print(isinstance(w_student,WorkingStudent))
print(isinstance(student,WorkingStudent))
print(isinstance(w_student,Student))
