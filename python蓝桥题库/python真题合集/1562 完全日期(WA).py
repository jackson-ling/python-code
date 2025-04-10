#一眼感觉会，但是卡了好久，卡在如何把每一个数字加起来

import datetime
cnt=0
tot=0
a=datetime.date(2001,1,1)
b=datetime.date(2021,12,31)
c=datetime.timedelta(days=1)

while a<=b:#如何再时间模块下用循环让日期累加？
    date = datetime.date.strftime(a, "%Y%m%d")
    for i in range(0,8):
        tot+=int(date[i])#又是考察字符串，转成整数，每一次遍历就累加一次，实现日期中的各位数字相加
    n=tot**0.5
    if n%1==0:#这里也需要学习，如何判断存不存在小数
        cnt+=1
    tot=0 #重点：每一次循环都要重置一次tot，只是暂存的一边变量记录总值
    a+=c
print(cnt)