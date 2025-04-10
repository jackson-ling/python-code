import math
n=int(input())
t=math.sqrt(5)
a=(1+t)/2
b=(1-t)/2
f=((math.pow(a,n)-math.pow(b,n))/t)
print('%.2f'%f)