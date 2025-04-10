#Counter（一个可迭代序列）   自动统计元素出现的个数
from  collections import Counter
li=[]
a=[1,2,3,4,4,5,6,2]
tot=Counter(a)
for i in tot.items():
  li.append(i)

print(li)
print(tot)

li1=[]
b="helloworld"
tot1=Counter(b)
for i in tot1.items():
    li1.append(i)

print(li1)
print(tot1)
