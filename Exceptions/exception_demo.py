
# try:
#     x  = 0
#     print(5/x)
#     print(4)
# except ZeroDivisionError:
#     print("Do not devide by zero")

# try:
#     with open("file.xyz","r") as file:
#         print(file)
#     print(5/0)
# except FileNotFoundError:
#     print("File could not be found")
# except ZeroDivisionError:
#     print("Zero division error occured") 


#custom exception
class InvalidEmailError(Exception):
    pass

def send_email(email,sbject,content):
    if not "@" in email:
        raise InvalidEmailError("Email does not contain an @")


try:
    send_email("hello","Subject","Content")
except InvalidEmailError:
    print("Please enter a valid e_mail address")
