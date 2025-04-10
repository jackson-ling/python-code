# 二分查找的前提：是有序的

# from bisect import *  表示导入bisect中所有的函数

import bisect

# 模块一：查找（bisect）

'''
查找（bisect）：传入（列表，需要查找的元素），返回元素的下标索引

重要！！！！！！！——————结果：都会返回如果把这个数插入列表中插入的位置索引

1.bisect_left：查找第一个

2.bisect_right：查找最后一个

3.如果查找的元素不在列表中，就会把该元素按有序的方式插入到列表中并返回插入的位置的下标索引(实际并不会插入)
'''

li=[1,2,2,3,4,5,6,7,8,9]

x=2
x1=10

left=bisect.bisect_left(li,x)
left1=bisect.bisect_left(li,x1)
print('查找的第一个位置是：%s，查找的是：'%left,x)   #  1
print('查找的第一个位置是：%s，查找的是：'%left1,x1)  #  10

x2=2

right=bisect.bisect_right(li,x2)
print('查找的最后一个位置是：%s，查找的是：'%right,x2)  #  3

# 返回的是如果在最后一个位置插入2，这个插入位置的下标索引（前提是有序的）

print('原列表是：%s'%li)

# 模块二：插入（insort）

'''
insort_left(有序的列表，插入元素)——插入到第一个位置

insort_right(有序的列表，插入元素)——插入到最后一个位置
'''

left2=bisect.insort_left(li,2)
left3=bisect.insort_right(li,2)
right2=bisect.insort_right(li,11)
print('插入后的列表是：%s'%li)