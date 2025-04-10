'''
二.datetime 模块（可以实现对时间加减）
类型：类比结构体
datetime.date():括号传递日期（年月日）
datetime.time():括号传递时间（时分秒）
datetime.datetime():括号传递日期时间
timedata:时间间隔



weekday（）使用：给一个具体的日期（date类型），可以返回今天周几（0表示周一）
t=datetime.date(2025,1,15)
a=t.weekday()
print(a)


获取当前日期
datetime.date.today()
datetime.datetime.now()
'''

import datetime
#获取当前日期和当前时间
print(datetime.date.today())#当前日期
print(datetime.datetime.now())#当前日期+时间

#模块的应用
a=datetime.date(2025,1,15)
b=datetime.time(18,7,15)
c=datetime.datetime(2025,1,15,18,7,15)
c1=datetime.datetime(2026,2,16,19,8,16)
d=datetime.datetime.combine(a,b)


print(a)
print(b)
print(c)
print(d)


print(a.year)
print(a.month)
print(a.day)


print(b.hour)
print(b.minute)
print(b.second)


#timedelta只能和datetime对象一起使用对时间加减
'''
时间间隔可以传入的参数
周，天，时，分，秒

注意：由于平年闰年天数不同，所以就没有年这个参数
'''
e=datetime.timedelta(weeks=1,days=1,hours=1,minutes=1,seconds=1)

print(c)#原来的时间

f=c+e
print(f)#间隔后的时间

g=f-c#时间间隔
print(g)  #8 days, 1:01:01

n=c1-c
print(n)#计算两个时间差

#时间差delta只能访问days和seconds
print(e.days)
print(e.seconds)


#字符串格式化
x=datetime.date(2025,1,15)
print(x.strftime("%Y-%m-%d"))
x1=datetime.date(2025,1,15).strftime("%Y-%m-%d")
print(x1)


#注意：x和x1的类型不一样，但是打印结果相同
print(x)
print(x1)
print(type(x))
print(type(x1))


#注意strptime格式(区别于time模块strptime用法)
x2=datetime.datetime.strptime("2025-1-15-18-7-15","%Y-%m-%d-%H-%M-%S")
print(x2)
print(type(x2))


#weekday()的使用
t=datetime.date(2025,1,15)
t1=t.weekday()
print(t1)#注意周一是0