import math
n=int(input())
m=0#初始化随条件变化变量值会变化的变量
for i in range(3):
    a,b=input().split()#如果对input（）强转int（）与split（）搭配会报错
    money=math.ceil(n/int(a))*int(b)
    if m==0 or money<m:#通过循环去遍历，每一次都对比。符合条件重新赋值
        m=money#对随条件变化变量值而改变的变量重新赋值，同时用新变量接受
print(m)
