def multi_print():
    print("Hello World")
    print("Hello World")

#multi_print()


#Function with params
def multi_print2(name):
    print(name)
    print("Given Name is: " + name)

#multi_print2("Gokhan")

def multi_print3(name,count):
    for i in range(0,count):
        print(name)

#multi_print3("Gokhan",5)

#Function with return
def maximum(x,y):
    if x > y:
        return x
    else:
        return y

#bigger_value = maximum(4,6)
#print(bigger_value)