from datetime import datetime,timedelta


now = datetime.now()

#dd.MM.yyyy
#%Y -> yyyy  %y -> yy
print(now.strftime("%d.%m.%Y"))

#add time values to datetime
print(now+timedelta(days = 20,hours=4))