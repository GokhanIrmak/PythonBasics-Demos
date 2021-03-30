#IMPORT Module Approach 1
# import Hello_Module as hm

# Hello_Module.world()
# Hello_Module.mars()


#IMPORT Module Approach 2 only import needed functions, * will import everything
# from Hello_Module import world,mars
# world()

#IMPORT Module Approach 3
# import matplotlib.pyplot as plt

# plt.plot([1,2,3],[5,4,5])
# plt.show()



# import ModulesFolder
# from ModulesFolder import file
#__init__.py file will let know the python that folder will be used as module

# from ModulesFolder import *
# if '*' will be used, "__init__.py" file should be edited and module will know what * means.

import ModulesFolder
#This will not work until you edit __init__.py file in module folder

ModulesFolder.file.f()
