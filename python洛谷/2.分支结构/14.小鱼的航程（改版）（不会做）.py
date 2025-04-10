x,n=[int(i) for i in input().split()]
tot=0
for i in range(1,n+1):#遍历第一题那到第n天
    if x!=6 and x!=7:
        tot+=250
    x%=7#七天一个星期轮回，假设是第八天，对7取余就知道今天是周一，小鱼要游泳
    x+=1#如果是第八天怎么知道是周几，让x自增来代替n的作用（表示过了几天）
    '''注意一个点，先对7取余在对x自增，反过来会影响取余的结果'''
print(tot)
















# x,n=map(int,input().split())
# # x代表周几开始游，n代表过了n天
# day=5-x+1#第一周游的天数
# a=n-day#代表第一周游的天数
# b=n-(5-x+1)#表示剩余的天数，n天分成两部分，一部分是第一周（不完整的周数），剩余的是完整的周数加上多余的天数
# c=b/7#计算有多少个完整的周数和多余的几天
# if c%10==0:
#     day1=c
#     distance=a*250+day1*250
#     print(int(distance))
# elif c%10!=0:
#     day1=c//10
#     day2=c%10#表示除了整数周还多出的天数、
#     distance=a*250+day1*250+day2*250
#     print(int(distance))
