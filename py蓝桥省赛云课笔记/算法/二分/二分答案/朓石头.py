'''
L:分别表示起点到终点的距离
N:起点和终点之间的岩石数
M:以及组委会至多移走的岩石数
Di：表示第i块石头和起点的距离
'''

L,N,M=map(int,input().split())
D=[]
for i in range(N):
    D.append(int(input()))

# 假设最短跳跃距离是x，移除的数量不超过M，则为合法
def check(x):
    # 定义移走的石头数量
    cnt=0

    # 根据合法的要求可以知道最后函数的返回值，中间部分就需要写--到底怎么移，移动多少？

    last=0  # 从0的位置开始朓，即初值为0  #记录上一个位置，进而引出跳跃距离

    #接着遍历每一块岩石，取判断跳跃距离
    for i in range(N):
        if D[i]-last>=x:# 表示能跳，跳过去就更新下标，接着就是后面的石头和和起点的距离-last和起点的距离=跳跃的距离
            last=D[i]
        else:
            cnt+=1  #把石头移走
    if L-last<x: # 要求的是最短跳跃距离
         cnt+=1
    return cnt<=M  #需要返回合法的条件

left,right=1,L  #求的是最短条约距离，取最小和最大
while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid-1

print(ans)