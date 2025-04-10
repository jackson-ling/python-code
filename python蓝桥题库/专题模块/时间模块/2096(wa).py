# 本题不会，首先没有想到枚举所有的顺子日期，然后没有注意到题目提示的是字符串，可以遍历和使用一些字符窜的方法

import datetime
start=datetime.date(2022,1,1)
end=datetime.date(2022,12,31)
delta=datetime.timedelta(days=1)
ans=0
m=['012','123']
while start<=end:
    a=start.strftime("%Y%m%d")
    for i in m:
        if i in a:
            ans+=1
            break
    start+=delta
print(ans)
