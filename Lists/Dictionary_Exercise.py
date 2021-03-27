names = {}
max_repeat = 0
max_repeat_name=""
with open("D:/Python/CourseMaterial/data/names.csv", "r") as file:
    for line in file:
        line_split = line.strip().split(",")
        if line_split[0] == "Id":
            continue
        if line_split[1] in names:
            names[line_split[1]] += int(line_split[5])
        else:
            names[line_split[1]] = int(line_split[5])
    print(names)

    for key,value in names.items():
        if value > max_repeat:
            max_repeat_name = key
            max_repeat = value
    print(max_repeat_name)
    print(max_repeat)
