N,K=map(int,input().split())
a=[]
for i in range(N):
    x,y=map(int,input().split())
    a.append((x,y))

left,right=1,100000

# 本题中是否合法是：给出的边长能否切出K块巧克力

# 最后返回合法的条件即可(会自动进行真假的判断,即返回0还是返回1)

def check(x): #假设切出巧克力的边长为X
    cnt=0
    for H,M in a:
        cnt+=(H//x)*(M//x)
    return cnt>=K

while left<=right:
    mid=(left+right)//2
    # 如何调整区间的变化取决于题目的问题
    if check(mid):
        ans = mid  # 优先更新答案
        # 本题要找最大，所以就是更新左区间，让值变大
        left=mid+1
    else:
        right=mid-1

print(ans)