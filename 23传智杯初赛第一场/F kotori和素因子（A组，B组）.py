# 判断素数的两种方法

# 第一种：定义函数(注意函数要有返回值)

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
     return n

# print(is_prime(2))
# 第二种：根据素数（质数）的定义遍历判断
# n=int(input())
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

def yinzi(x):
    lix=[]
    for i in range(1,x+1):
        if x % i ==0:
            lix.append(i)
    return lix

print(yinzi(21))



a=int(input())
li=[int(i) for i in input().split()]#输入的四个数
li1=[]#存放素数因子（没有去重）
li2=[]#存放去重后的素因子
#找出每个数的素因子，而且不同数的素因子不能相同
# 1.先找出因子
# 2.冲因子里挑选素数
# （1.2就是判断，用 and）
# 3.打印每个数的素因子，创建列表，除重处理
# 4.放到一个新的列表，运用函数求出最小的两个数相加求和
# for i in li:
#     if i%j==0:
#         print(j)
