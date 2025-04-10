dit={'a':1,'b':2,'c':3}
dit1={'aa':10,'bb':22,'cc':33}
# 取值
print(dit.keys())
print(dit.values())
print(dit.items())

#遍历
for i in dit.keys():
    print(i)

for i in dit.values():
    print(i)

for x,y in dit.items():
    print(x,y)

#删除
dit.pop('a') #要传入一个键值，输出的是键值对
del dit['b']
dit.popitem() #默认删除最后一对

#统计元素个数
print(len(dit))

#字典合并
dit.update(dit1)

li=[1,2,3]
li1=['a','b','c']
dit2=dict(list(zip(li,li1))) #zip(键,值)
print(f'dit2={dit2}')

#字典取值
x=dit2.get(1)
print(f'x={x}')