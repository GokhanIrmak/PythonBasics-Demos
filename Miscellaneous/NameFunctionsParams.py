
#Default value params, 
#If function will be called as multi_print(), it will work
def multi_print(number = 3,word = "MyWord"):
    for i in range(0,number):
        print(word)

# multi_print() -> This will work with default values
# multi_print(5) -> This will assign 5 as number
# multi_print("Hello") -> This will give error because of order
# multi_print(word="Hello") -> This will work with "Hello" an default number
# multi_print(word="Hello",number=5) -> Will work with params given



