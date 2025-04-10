#方法一
import datetime

start_time = datetime.date(1949, 10, 1)
end_time = datetime.date(2012, 10, 1)

cnt = 0

for year in range(start_time.year, end_time.year+1):
    nationalday = datetime.date(year, 10, 1)
    if nationalday.weekday() == 6:
        cnt += 1

print(cnt)



#方法二
a=datetime.date(1949,10,1)
b=datetime.date(2012,10,1)
cnt=0
while a<=b:
  if a.weekday()==6 and a.month==10 and a.day==1:
    cnt+=1
  a+=datetime.timedelta(days=1)
print(cnt)

