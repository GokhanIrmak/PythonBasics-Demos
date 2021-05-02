
#Curly brackets like dictionary but not key:value pairs
my_set = {"Hello","World"}
#not append but add
my_set.add("Mars")

#Set will decide its order, no specific rules
print(my_set)

if "Mars" in my_set:
    print("Mars is in the set")


#Set will store a value only once....
text = "Hello World Hello Mars Hello World"
words = set()
for word in text.split(" "):
    words.add(word)
print(words)