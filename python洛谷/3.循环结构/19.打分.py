# 易错点：pop删除的是列表的索引，而不是某个具体对象
n=int(input())
li=[int(i) for i in input().split()]
li.sort()
li.pop(0)
li.pop(len(li)-1)
average=sum(li)/len(li)
print('%.2f'%average)






# 报错代码：
# n=int(input())
# li=[int(i) for i in input().split()]
# li.pop(max(li))
# li.pop(min(li))
# average=sum(li)/len(li)
# print(average)