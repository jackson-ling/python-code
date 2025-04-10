#认真审题，题目要求  最长，说明有多个连号

n=int(input())
li=[int(i) for i in input().split()]
maxn=0#连号可能有很多个，记录最大的那个长度，初始化为0
for i in range(n):
    cnt = 0#记录单个连号长度，初始化为0
    for j in range(i+1,n):
        if li[j]==li[j-1]+1:#重点:连号的定义怎么表达
            cnt+=1
        #注意：if--else语句要写完整
        else:
            break
    maxn=max(maxn,cnt)#取两个连号中的最大值
print(maxn+1)#易错，这里自增一次表示二者之间的比较，最终长度还要加上连号的第一个数（+1）