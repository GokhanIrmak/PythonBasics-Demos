# class Student():
#     pass

# eric = Student()
# eric.firstname="Erik"
# eric.lastname="Miller"

# print(eric.firstname)
# print(eric.lastname)

# METHOD
# class Company:
#     def get_name(self):
#         print(self.legal_name + " " + self.legal_type)


# c = Company()
# c.legal_name = "Max Miller"
# c.legal_type = "Ltd."

# #get_name(c)
# c.get_name()

# CONSTRUCTOR

class Student():
    # Constructor
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # self.term = 1
        self.__term = 1 #--> this double underscore will make "term" private
                        #--> Direct assignments will be ignored

    def get_term(self):
        return self.__term

    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term += 1

    def get_name(self):
        print(self.firstname + " " + self.lastname + " " +str(self.__term))
    #one underscore is warning to developer, double underscore is private
    def __get_lastname(self):
        print("111111" + self.lastname)

    #SPECIAL METHODS
    #toString()
    def __str__(self):
        return "Student("+self.firstname + " " + self.lastname + " " +str(self.__term)+")"

    # normally represents object type and location in stack, but we can override
    def __repr__(self):
        #return "Student("+self.firstname + " " + self.lastname + " " +str(self.__term)+")"
        return.self.__str__()
    def __len__(self):
        return len(self.firstname)+len(self.lastname)




eric = Student("Eric", "Miller")
eric.get_name()
eric.__term = 100 ##--> This assignment will be ignored,
print(eric.get_term())
print(eric)
print(len(eric))
eric.increase_term()


# monika = Student("Monika", "Fisher")
# monika.get_name()
