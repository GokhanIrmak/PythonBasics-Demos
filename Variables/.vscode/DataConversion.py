a = "5"
b = "6"

# String -> Integer
print(a + b)
print(int(a) + int(b))

# String->Floating Numbers
v = "5.5"
g = "6.2"
print(float(v)+float(g))

# Integer -> String
age = 26
print("I'm " + str(age) + " years old.")

# List -> String
students = ["Max", "Monica", "Erik", "Franziska"]
students_as_string = ", ".join(students)
print("#".join(students))
print(", ".join(students))
print("Converted String: " + students_as_string)

# String -> List
print(students_as_string.split(", "))
sentence = "I am a sentence with many words"
print(sentence.split(" "))
print(len(sentence.split(" ")))