n,m=map(int,input().split())
r,c=map(int,input().split())
li=[[0]*m for i in range(n)]

x,y=0,0
value=1
li[x][y]=value

while value<n*m:
    #往右走
    while y+1<m and li[x][y+1]==0:# 保证不越界，并且下一个位置的值不可以有其他值
        y+=1
        value+=1
        li[x][y]=value
    #往下走
    while x+1<n and li[x+1][y]==0:
        x+=1
        value+=1
        li[x][y]=value
    #往左走
    while y-1>=0 and li[x][y-1]==0:
        y-=1
        value+=1
        li[x][y]=value
    #往上走
    while x-1>=0 and li[x-1][y]==0:
        x-=1
        value+=1
        li[x][y]=value
print(li[r-1][c-1])