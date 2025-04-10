# 如何用循环来比较鱼之间的可爱程度----这个循环逻辑不会
n=int(input())
li=[int(i) for i in input().split()]
li1=[0]#设置可爱度列表，第一只小鱼可爱度为0
for i in range(1,n):#遍历除了第一只其他剩下的所有鱼（注意列表第一只鱼索引为0）
    cnt=0#设置比自己可爱的鱼的数量初始化为0
    for j in range(i):#重点：从开始遍历到当前位置
        if li[i]>li[j]:
            cnt+=1
    li1.append(cnt)
for c in li1:
    print(c,end=' ')
