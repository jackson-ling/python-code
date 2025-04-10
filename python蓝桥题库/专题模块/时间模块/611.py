import datetime
start=datetime.date(1901,1,1)
end=datetime.date(2000,12,31)
delta=datetime.timedelta(days=1)
ans=0
while start<=end:
    if start.weekday()==0:
        ans+=1
    start+=delta

print(ans)