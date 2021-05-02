l=["Max","Monica","Eric","Paula"]
l.sort() #Alphabetical sort
# print(l)

l.sort(reverse=True) #reverse sort
# print(l)

# len is not used as len() here, just function name
l.sort(key=len) #Sort by length of the item - From shortest to longest
#print(l)


d={"Cologne":"CGN","Istanbul":"IST","Budapest":"BUD"}
#print(sorted(d,reverse=True)) # Will Print keys sorted reversed

#Sorted will return sorted list but will not edit the original


