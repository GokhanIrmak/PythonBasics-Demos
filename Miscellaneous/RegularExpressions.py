import re

sentence = "I have 30 dogs that need 4 litres of water and 2 kg of food each."

#charcters between 0-9 and it can be more than one

print(re.findall("[0-9]+",sentence))

#Find the fist match
print(re.search("[0-9]+",sentence))

#last character "e" is optional
print(re.search("have?",sentence))

#last character "e" is has to be there 0 or more times
print(re.search("the*","Hello the hello"))

#last character "e" is has to be there 1 or more times
print(re.search("the+","Hello the hello"))

#Find the fist match
print(re.search("[0-9]+",sentence))