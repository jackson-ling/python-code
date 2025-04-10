'''

写一个函数判断是否合法
def check(x):
    #判断x是否合法，合法返回True，否则返回False
    pass

left,right,ans=初始化

while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=mid  优先更新答案
        left=mid+1    # 根据题目来判断调整左区间还是右区间，语句固定，知道一个的位置
                        也就知道了
    else:
        right=mid-1

本模板是求最大的情况，区间向大的靠近

print(ans)


说明：这是一个模板，唯一要变的只有 1.check函数的判断时候合法  2.left=mid++1 语句的位置


显然使用二分的
1.有单调性：一个量变化的同时另一个量也跟着变化，同时有线性关系
2.最小值最大化，最大值最小化(最值问题+单调)
3.第k小问题
'''