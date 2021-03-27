# %matplotlib inline
import matplotlib.pyplot as plt

# xs=[1,2,5]
# ys=[4,7,5]

# plt.plot(xs,ys)
# plt.show()

xs=[]
ys=[]
name = "Max"
gender = "M"
state = "CA"
low_year = 1950
high_year = 2000
occurences = 0
with open("D:/Python/CourseMaterial/data/names.csv", "r") as file:
    for line in file:
        line_split = line.strip().split(",")
        if line_split[1] == name and line_split[3] == gender and line_split[4] == state and int(line_split[2])>= low_year and int(line_split[2])<=high_year:
            occurences += int(line_split[5])
            xs.append(int(line_split[2]))
            ys.append(int(line_split[-1]))
print(occurences)
plt.plot(xs,ys)
plt.show()