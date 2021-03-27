# DICTIONARIES

d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
# print(d)
# Access element
# print(d["Helsinki"]) #If key doesn't exist it will throw KeyError
# print(d.get("Saigon")) # If key doesn't exist it will return None

# Add element to the dictionary
d["Budapest"] = "BUD"
# print(d)

# Delete an element
del d["Budapest"]
# print(d)

# if "Budapest" in d:
#    print("Budapest is included in the dictionary")
# if "Saigon" in d:
#    print("Saigon is included in the dictionary")

d={"Munich":"MUC","Budapest":"BUD","Helsinki":"HEL"}
for key in d:
    value=d[key]
    print(value)
    print(key)

print(d.items())#-->Will return dict. items as tuple

for key,value in d.items():
    print(key + ": " + value)

# TUPLES
t = (1, 2, 3)
# t.append() or add() not gonna work because tuples are constant.
person = ["Max Muller", 55]


def do_something(p):
    p[0] = "Max Mustermann"


# print(person)
do_something(person)
# print(person)

tuple_person = ("Max Muller", 55)
# do_something(tuple_person) # Will throw an error because tuples are immutable

student = ("John Doe", 22, "Informatics")
# name=student[0]
# age=student[1]
# subject=student[2]


def get_student():
    return("John Doe", 22, "Informatics")


# There should be exact amount of variables in both side.
# 3 variables in tuples so 3 variables will be created, if different, this won't work
# Same assignments as above. Will Assign in order
name, age, subject = get_student()

print(name)
print(age)
print(subject)


print(get_student())


# List of tuples
students = [("Max Miller", 22),
           ("Monika Fisher", 25),
           ("Frank Johnson",23)]

for name,age in students:
    print(name)
    print(age)