# def f(a,b,c,):
#     print(a)
#     print(b)
#     print(c)

# l=[1,2,3]

# #Result will be the same in both
# #That is because amount of variables equals to params
# #If different then error thrown
# f(l[0],l[1],l[2])
# f(*l)





# #flexible amount of parameters
# def calculate_max(*params):
#     print(params)
# #    print(params[0])
#     current_max = params[0]
#     for item in params:
#         if item > current_max:
#             current_max = item

#     print(current_max)
# #Params stored in tuple
# calculate_max(1,2,3,5,7,8,3)

#This is also available, first given value will be current_max
# def calculate_max(current_max,*params)


# #"**"" is for dictionary
# def f(**args):
#     print(args)

# f(key="value",key2="value2")



import matplotlib.pyplot as plt

def create_plot(**plot_params):
    print(plot_params)
    #color or thickness etc.
    plt.plot([4,2,6],[5,8,3],**plot_params)
    plt.show()

create_plot(color="r",linewidth=7,linestyle = "dashed")