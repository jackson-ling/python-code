from datetime import datetime,timedelta
s,v=map(int,input().split())
if s%v==0:
    t=s//v
else:
    t=s//v+1  #如果有多出来的秒数时间上直接加一分钟，预留了时间肯定能到

# 10分钟垃圾分类时间去除掉，那么计算中可以不携带，就算成7点50
# 随便设置一个 7点50的datetime
t1 = datetime(year=2024,month=10,day= 24,hour=7,minute=50)

# 设置一个timedelta，时间设置为上面算出来的t，即为上学需要的用时
t2 = timedelta(minutes=t)

# 那么t1 - t2求出来的datetime就是最晚出发时间
t3 = t1 - t2

# 把datetime改变成输出的样式的字符串
t4 = t3.strftime("%H:%M")

print(t4)


