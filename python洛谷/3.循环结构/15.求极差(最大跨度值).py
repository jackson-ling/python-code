# 运用极差定义：最大值减去最小值
# n=int(input())
# li=[int(i) for i in input().split()]
# print(max(li)-min(li))


#先对数字排序，之后去取第一位和最后一位
n=int(input())
li=[int(i) for i in input().split()]
li.sort()
print(li[len(li)-1]-li[0])
