# 思路欠缺：如果一个数能被拆解成多个数相乘，那末这些数字一定是这个数字的----因数

n=int(input())
# 判断素数
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True


for i in range(2,n+1):
    if n%i==0:#重点：如果能被n整除，说明i是n的一个因数
        if is_prime(i) and is_prime(n//i):
            #重点：
            # 1.前提是改因数是质数
            # 2.i是从小到大开始遍历的，那么求出来的一定是最大的因数
            print(n//i)
            break

#我的思路：先判断是不是质数，然后用枚举法把因数找出来，之后求出因数的最大值
