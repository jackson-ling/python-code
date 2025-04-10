#列表的补充内容（蓝桥云课）

# 1.列表的操作

# 循环遍历列表
# li=[]
# for i in li:
#     print(i)

# 循环遍历列表并显示 元素和元素对应的下表，生成一个序列（enumerate函数）
li1=['a','b','c']
for index,x in enumerate(li1):
    print(index,x)
# 0 a
# 1 b
# 2 c

#快速创建列表(强制类型转换)
li2=list(range(0,6))
print(li2)
li3=list(range(0,6,2))
print(li3)

#列表的拼接
li4=li2+li3
print(li4)

# 列表内置函数
a=sum(li4)
b=max(li4)
c=min(li4)

# 列表的复制
li1=['a','b','c']
d=li1.copy()
d[0]='c'
print(f'li1={li1}')
print(f'd={d}')

#列表推导式
# n=[对象的表现形式（数据类型，x**2等） for x in range()  if （可以附加判断条件）]
n=[x**2 for x in range(11) if x%2==0]
print(n)


                                        #列表的常用方法

# 索引和切片：和字符串一样


#index()查找一个对象，返回下表索引
a1 = [1,'a', [2, 5]]
print(a1.index(1))

#count()统计某个元素出现的次数
print(a1.count(1))


#列表元素的修改


#列表元素的添加(append()只能添加一个元素（对象），extend（）会先遍历再添加)
a11 = [1,2]
b11 = [3,4]
c11 = [5,6]

a11.append(b11)
print(a11)
c11.extend(b11)
print(c11)


#列表中插入元素（指定下标索引，插入元素，超出索引范围添加在末尾）
c12 = [0, 1, 2]
c12.insert(2, "嘿")
print(c12)			# [0, 1, '嘿', 2]


'''
列表元素的删除

1.del()

a = ["a","b","c","d","e"]
del a[2]  
del a[1:3]
print(a)			# ['a', 'b', 'd', 'e']

del a  删除列表，此时列表无定义

2.clear()  清空列表

3.pop（）  默认删除最后一个元素，括号中指定下标索引并返回删除的对象

注意：这是一个操作过程，返回结果需要用变量接收

a.pop()
b=a.pop(2)
print(b)

4.remove() 删除指定对象，如果有多个，删除第一个
'''

'''
列表元素的排序(后面有ed的代表不修改原列表的内容)
1.sort()   a.sort()  从小到大排序
 
2.sorted() b=sorted(a)

3.reverse()  a.reverse()  列表逆序输出

4.reversed()  b=reversed(a)

5.sort(reverse=True)   排序好后从大到小输出
 
'''