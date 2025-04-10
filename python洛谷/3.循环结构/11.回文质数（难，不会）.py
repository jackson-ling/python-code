a,b=int(input())
# 质数判断
def is_prime(x):
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True

