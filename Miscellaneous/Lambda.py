students = [
    ("Max",3),
    ("Monica",2),
    ("Eric",3),
    ("Paula",1)
    ]

#sort by semester
def students_key(student):
    return student[1]

students.sort(key=students_key)
print(students)

#Same funtvtionality with lambda
students.sort(key=lambda student:student[1])
print(students)

