'''

1.需要从functools中导入包--cmp_to_key
2.自己写一个自定义排序规则的函数cmp
3.在排序函数sort()中传入参数，key=cmp_to_key(自定义排序的函数)
例如：li.sort(key=cmp_to_key(cmp))

注意：内置定义了如果返回值是负数，表示把传进来的  第一个  参数排在前面，否则排在后面
     如果返回0表示按照sort的规则排序（二者相等返回0）

'''



from functools import cmp_to_key

li=[9,-2,-5,1,-6,4,7,3,-8]

# 案例一：按照绝对值从小到大排序
def cmp(a,b):
    if abs(a)<abs(b):
        return -1  #返回负数，传入的第一个参数排在前面
    elif abs(a) > abs(b):
        return 1   #返回负数，传入的第一个参数排在后面
    else :
        return 0

li.sort(key=cmp_to_key(cmp))
print(li)


# 案例二：给一个二元组，和小的在前，如果和相等，两个元组中第一个元素小的在前面
li1=[(2,3),(5,-2),(4,5),(5,0),(4,1)]

def cmp(a,b):
    if sum(a)<sum(b):
        return -1
    elif sum(a)>sum(b):
        return 1
    else:
        if a[0]<b[1]:
            return -1
        elif a[0]>b[0]:
            return 1
        else:
            return 0
x=sorted(li1)
li1.sort(key=cmp_to_key(cmp))

#二元组默认排序是按照第一个数字的大小做小到大排序

print(x)  # [(2, 3), (4, 1), (4, 5), (5, -2), (5, 0)]

print(li1) # [(5, -2), (2, 3), (5, 0), (4, 1), (4, 5)]




