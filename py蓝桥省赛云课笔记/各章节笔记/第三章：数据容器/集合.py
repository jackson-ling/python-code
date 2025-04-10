#集合（set）元素唯一，不可变
a={1,2,3}
b={1,2,3,4}

#遍历
for i in a:
    print(i)

#集合关系
print(f'交集={a&b}') #交集
print(f'并集={a|b}') #并集

'''
基本操作
1. a.add():一个对象
2. a.pop()：默认删除第一个，不能指定对象
3. a.remove():指定删除元素
4. a.clear():清空集合
'''

#重点：集合有自动去重功能
li=[1,1,2,2,3,3,4,4,5]
li1=[]
n=set(li)
for i in n:
    li1.append(i)
print(f'li={li}')
print(f'li1={li1}')