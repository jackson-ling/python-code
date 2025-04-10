n,m=map(int,input().split())  # n行m列

# 创建一个二维列表
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))

ans=0

#for循环暴力遍历  (只有确定了第一个格子的前提下去找第二个格子才不会遗漏可能的情况，所以用嵌套循环)
for i in range(n):
    for j in range(m):
        for ii in range(n):
            for jj in range(m):
                if li[i][j]==li[ii][jj] and abs(i-ii)==abs(j-jj) and abs(i-ii)>0:
                    ans+=1
print(ans)

