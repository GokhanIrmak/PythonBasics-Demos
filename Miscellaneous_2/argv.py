import sys

# user_input = input("Please enter something")
# print(user_input)
# print(sys.argv)

if len(sys.argv) >= 2:
    #print("More than just the file")
    filename = sys.argv[1]
    file = open(filename, "r")

    counter = 0
    for line in file:
        counter += 1

    print(counter)
