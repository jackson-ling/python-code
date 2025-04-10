'''
小明从a时b分开始游泳，到c时d分停止，输入4行，分别为a,b,c,d，
输入一个整数表示小明的有用时间（单位为分钟）
'''

#逻辑上遗漏了情况
print("欢迎进入小明游泳时间计算系统，默认晚上12点的小时单位输入24")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if c==a and d>b:#同一个小时的情况
    print(d-b)
elif c>a and d>=b:#跨小时分钟可以相减，但是遗漏了‘’分钟有相等的情况‘’
    time=(c-a)*60+(d-b)
    print(time)
elif c>a and d<b:#跨小时情况
    t1=(c-a-1)*60
    t2=60+d-b
    time=t1+t2
    print(time)
elif c == a and d == b:  # 时间完全相同的情况
    print("小明并没有游泳")
else:
    print("输入时间不符合常理，请重新输入")