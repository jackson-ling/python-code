'''
一.time 模块（不可以对时间加减计算,但是可以计算sleep后时间戳的差值）

包含三个板块:
1.时间戳：s=time.time()
2.获取当地时间：time.localtime()
3.time.sleep（x）

时间方法：
1.时间转字符串：time.strftime()
2.字符窜你转时间：time.strptime()

'''

import time

#time模块

a=time.time() #获取时间戳（自1970-1-1 00:00）
print(a)

time.sleep(1)

b=time.time()
print(b)

print('{:.0f}'.format(b-a))#保留0位小数就是取整
# print("%d" % (b-a))

c=time.localtime()#获取当前时间，类型是一个结构体（time.struct_time）
print(c)
print(type(c))

# 打印 struct_time 的各字段
print("c = ", c)
print("年份 = ", c.tm_year)   # 4位数年份
print("月份 = ", c.tm_mon)    # 1-12
print("日期 = ", c.tm_mday)   # 1-31
print("小时 = ", c.tm_hour)   # 0-23
print("分钟 = ", c.tm_min)    # 0-59
print("秒 = ", c.tm_sec)      # 0-61
print("一周的第几天 = ", c.tm_wday)  # 0-6，0是周一
print("一年的第几天 = ", c.tm_yday)  # 1-366
print("夏令时标识 = ", c.tm_isdst)   # 夏令时标识

#日期的格式化
d=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())#打印当前的时间
print(d)

e=time.strptime(d,"%Y-%m-%d %H:%M:%S")
print(e)
