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


student=WorkingStudent("John","Doe","ABC Company")
print(student.name())