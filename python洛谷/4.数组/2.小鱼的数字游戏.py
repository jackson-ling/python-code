li=[int(i) for i in input().split()]
li.pop(len(li)-1)
li.reverse()
for i in li:
    print(i,end=' ')
'''
关于删除最后的数据方法
'''
 # 1.pop()  删除指定下标的数据(默认为最后一个)
 # 2.运用列表索引  li.pop(len(li)-1)  （注意：第一个数据索引为0，长度要减一）
 # 3.运用步长为负值  li.pop(-1)