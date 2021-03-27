# --File Read
file = open("D:\\Python\\PythonBasics-Demos\\Hello\\.vscode\\read.txt", "r")
# for line in file:
#     print(line.strip())

file.close()

# --File Write
file = open("D:\\Python\\PythonBasics-Demos\\Hello\\.vscode\\write.txt", "w")
#file.write("File Writing\n")
# file.write("SecondLine")

# students = ["Max","Monika","Erik","Franziska"]
# for student in students:
#     file.write(student+"\n")

file.close()


# --Append Data to File
file = open("D:\\Python\\PythonBasics-Demos\\Hello\\.vscode\\append.txt", "a")
# students = ["Max","Monika","Erik","Franziska"]
# for student in students:
#     file.write(student+"\n")

# file.write("End of Students")
file.close()

# --Wıth Construct
# File will be closed when code goes out of the indentation
# with open("D:\\Python\\PythonBasics-Demos\\Hello\\.vscode\\read.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# --Working with CSV files
with open("D:\\Python\\PythonBasics-Demos\\Hello\\.vscode\\demo_data.csv") as file:
    for line in file:
        data = line.strip().split(";")
        #print(data[0]+":"+data[1])
        if(data[2]=="BER" or data[2]=="BUD"):
            print(data[0])