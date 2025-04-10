#方法一
# a=int(input())
# b=int(input())
# t=int(input())
# h=(b+t)//60
# m=(b+t)%60
# print(a+h)
# print(m)

#没想到的地方：把输入的分钟单独拿出和间隔的分钟放在一起求过了t分钟后的是几点


# 方法二：遇到时间的题目套时间模块就行----模板题目
import datetime
a=int(input())
b=int(input())
t=int(input())
start=datetime.datetime(2025,1,16,a,b)
x=datetime.timedelta(minutes=t)
end=start+x
print(end.hour)
print(end.minute)