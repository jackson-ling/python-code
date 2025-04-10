n,m=map(int,input().split())
a=[]
for i in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)
b=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        tot=0
        cnt=0
        for deltax in [-1,0,1]:
            for deltay in [-1,0,1]:
                x=i+deltax
                y=j+deltay
                # 判断是否越界
                if 0<=x<n and 0<=y<m:
                    tot+=a[x][y]
                    cnt+=1
        b[i][j]=tot//cnt
for i in b:
    print(*i)