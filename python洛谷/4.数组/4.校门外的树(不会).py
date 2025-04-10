l,m=[int(i) for i in input().split()]
#创建二维列表记录区间
li=[[int(i) for i in input().split()] for i in range(m)]#生成一个二维列表记录范围
a=[1 for i in range(l+1)]#生成一个每个数据都一样的列表，1循环l+1次
for c in li:#遍历没有树的范围
    for i in range(c[0],c[1]+1):#左闭右开，注意+1
        a[i]=0#新思路，这个范围没有树，直接为 0即可-----不用计算出该范围数的数量，再用总数量去减掉
print(a.count(1))

# 巧处：每棵树有编号（第二棵树是2），但是目的是算出属的数量，干脆列表数据一样，用count（）统计即可