# translations = {
#     "number_of_dogs":"I have XXX dogs"
# }

# print(translations["number_of_dogs"].replace("XXX",str(5)))


translations = {
    "number_of_dogs":"I have {0} dogs"
}

print(translations["number_of_dogs"].format(5))
print("I have {0} {1} {0} dogs".format(5,"Cats "))
print("I have {number:.3f} {animals}".format(number=6,animals="Cats"))