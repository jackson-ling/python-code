import math
pi=3.14
h,r=map(int,input().split())
v=(pi*r**2*h)/1000
count=(20/v)
print(math.ceil(count))
