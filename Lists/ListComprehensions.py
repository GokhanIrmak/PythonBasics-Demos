#xs=[1,2,3,4,5,6,7,8]

#ys=[]
#for x in xs:
#    ys.append(x*x)

#ys=[x*x for x in xs] # Same as above for loop


# students=["Max","Monika","Erik","Franziska"]
# lengths=[len(student) for student in students]
# print(lengths)

import matplotlib.pyplot as plt

xs=[x/10 for x in range(0,100)]
ys=[x*x for x in xs]

plt.plot(xs,ys)
plt.show()
