import math
a,b,c=(input().split())
a=float(a)
b=float(b)
c=float(c)
p=1/2*(a+b+c)
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(float(f'{s:.1f}'))


