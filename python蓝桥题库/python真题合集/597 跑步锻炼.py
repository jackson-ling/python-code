import datetime

a=datetime.date(2000,1,1)
b=datetime.date(2020,10,1)
c=datetime.timedelta(days=1)

tot=0

while a<=b:#
    if a.weekday()==0 or a.day==1:#易错易错：周一是从0开始算的
        tot+=2
    elif a.weekday()==0 and a.day==1:
        tot+=2
    else:
        tot+=1
    a+=c

print(tot)