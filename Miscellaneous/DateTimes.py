from datetime import datetime,time,date

now = datetime.now()
print(now)

#20th of August 2018
day = datetime(2018,8,20)
print(day)

d=date(2018,8,20)
print(d)

t=time(20,1,4)
print(t)

my_dt = datetime.combine(d,t)
print(my_dt)
