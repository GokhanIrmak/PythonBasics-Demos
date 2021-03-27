students=["Max","Monika","Erik","Franziska"]

#POP will remove last element from the list
#and return it if you want to store the value 
last_student=students.pop()
print(last_student)
print(students)

#Remove element From list
#Combine two lists
students2=["Max","Monika","Erik","Franziska"] + ["Frank"]
print(students2)

del students2[3]
print(students2)

students2.remove("Monika")
print(students2)

#[-1] [-2] ... get element from last to first
students3=["Max","Monika","Erik","Franziska"]
print(students3[-1])

#List Slicing
students_sliced=["Max","Monika","Erik","Franziska","Frank"]
print(students_sliced[2:4])
#Will return Erik and Franziska from 2 to 4, exclude 4
print(students_sliced[1:3])
print(students_sliced[0:-1]) #Everything but last one
print(students_sliced[:-1])#Same with above- if you have 0, no ned to write
print("Hello World"[0:5]) #--> Hello
print("Hello World Trial"[-5:])#--> Trial