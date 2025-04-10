n,k=[int(i) for i in input().split()]
ls1=[]
ls2=[]
for i in range(1,n+1):
    if i%k==0:
       ls1.append(i)
    else:
        ls2.append(i)
print("%.1f %.1f" % (sum(ls1)/len(ls1),sum(ls2)/len(ls2)))
#新思路：不用变量去接受变化的值，可以添加到列表进行计算