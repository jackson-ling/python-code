#注意审题，x是有范围的

n=int(input())
res=[]
def find_x_k(n):
    for x in range(1,101):
        for k in range(1,n):
            total=52*(7*x+21*k)
            if total==n:
                res.append((x,k))
    res.sort()
    return res[-1]
x,k=find_x_k(n)
print(x)
print(k)