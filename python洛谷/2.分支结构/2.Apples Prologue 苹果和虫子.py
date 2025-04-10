import math
m,t,s=map(int,input().split())
# 注意：1<=m<=100,0<=t<=100,1<=s<=10000

#m个苹果，吃一个花t分钟，吃完吃下一个，过去了s分钟，问还剩几个苹果？
# 吃了多少个苹果
v=s/t
b=math.ceil(v)
#剩余的a
a=m-b
if t==0:
    print(0)
else:
 print(a)
#错误点：
# 1.没考虑到t=0，就是秒吃，直接没了
# 2.没有考虑v可能是小数，就是吃了但是没吃完，不是一个完整的苹果
# 3.在t！=0的情况还要考虑苹果吃没吃完，用小于0来说明苹果吃完了


#正确的代码
import math
m,t,s=map(int,input().split())
if t==0:
    print(0)
else:
    a=m-math.ceil(s/t)
    if a<=0:
        print(0)
    else:
        print(a)
