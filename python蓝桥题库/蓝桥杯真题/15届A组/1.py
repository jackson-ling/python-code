import math

left=1
right=7385137888721*2+10470245

def check(x):
    a=math.sqrt(x)
    if a%10==0:
        return True

ans=-1
while left<=right:
    mid=(left+right)//2
    if check:
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)